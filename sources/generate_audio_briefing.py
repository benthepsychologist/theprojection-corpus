#!/usr/bin/env python3
"""Generate a daily audio briefing (mp3) from the front-page digest.

    python3 sources/generate_audio_briefing.py [--date YYYY-MM-DD] [--out DIR]

WHY THIS FILE EXISTS (2026-08-13). Ben asked for a daily audio briefing,
starting with the front/general feed. Two paths exist side by side on the
site: a zero-generation "Listen" button (theprojection-site's listen.js,
browser speechSynthesis, no file produced) and this — a real mp3, narrated
once a day in a fixed voice, for anyone who wants better quality than
whatever TTS engine their own device happens to ship.

WHAT THIS NEEDS TO RUN (not yet baked into a shared image, so document it
here rather than let it go tribal):
  - A Python venv with `kokoro` + `soundfile` installed — see
    /workspace/.venvs/kokoro-tts (NOT inside any git repo: this is local
    build tooling, not instance data, same reasoning as gitignoring
    artifacts/read/ derived output). ~5.2 GB on disk (kokoro pulls in
    torch/transformers/spacy as real dependencies, not optional extras —
    that weight is real, not a config mistake).
  - System `espeak-ng` (`sudo apt-get install -y espeak-ng`) — kokoro's
    phonemizer (misaki -> espeakng-loader) ships a hardcoded path from ITS
    OWN CI build environment that doesn't exist on a fresh machine
    ("/home/runner/work/espeakng-loader/..."); the two env vars below
    override it to the real system install. Confirmed broken without this
    fix, confirmed working with it, same session, both re-tested directly.
  - System `ffmpeg`, for the wav -> mp3 conversion at the end (kokoro/
    soundfile only writes wav; nothing in this pipeline writes mp3
    natively).

Run it with:
    /workspace/.venvs/kokoro-tts/bin/python3 sources/generate_audio_briefing.py

WHAT IT DOES: reads the given day's front digest
(artifacts/digests/daily/<date>-front.md), strips it down to clean speakable
prose (deliberately the same category of cleanup as ~/bin/spoken-extract's
clean_for_speech() — strip markdown/headers/links/emoji, keep plain
sentences — this is a second, independent implementation, not a shared
import, since spoken-extract lives on a different machine entirely and
narrates live chat, not a file), synthesizes it with Kokoro (voice
af_heart, American English), and writes an mp3 to the given output
directory (default: this repo's own artifacts/audio/, from which a
publish step is expected to copy it into theprojection-site's static/).

NOT YET WIRED INTO /daily OR tools/publish.py — this is a manual/callable
script today, not an automated pipeline step. Wiring it into the actual
publish flow touches kestrel's publish/adapter.py (engine code, out of
this repo's write zone) — flag as a follow-up brief, don't build it here.
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIGESTS_DIR = REPO_ROOT / "artifacts" / "digests" / "daily"
DEFAULT_OUT_DIR = REPO_ROOT / "artifacts" / "audio"

# Same override this file's own docstring explains: kokoro's phonemizer
# ships a build-time path from its own CI runner that doesn't exist here.
os.environ.setdefault(
    "PHONEMIZER_ESPEAK_LIBRARY", "/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1"
)
os.environ.setdefault(
    "ESPEAK_DATA_PATH", "/usr/lib/x86_64-linux-gnu/espeak-ng-data"
)


def clean_for_speech(text):
    """Markdown -> plain speakable prose. Independent of, but the same
    category of cleanup as, ~/bin/spoken-extract's clean_for_speech()."""
    # Drop YAML frontmatter.
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    # Drop fenced code blocks and inline code markers (keep the content).
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = text.replace("`", "")
    # Headers -> just the text.
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
    # Links [text](url) -> text; bare autolinks dropped.
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<https?://[^\s>]+>", "", text)
    # Bold/italic markers stripped, text kept.
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    # List markers -> nothing (the sentence itself carries the content).
    text = re.sub(r"^[-*]\s+", "", text, flags=re.MULTILINE)
    # Horizontal rules and blockquote markers.
    text = re.sub(r"^(---|___|\*\*\*)\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)
    # Em dash reads oddly through TTS in some voices; comma is a safe,
    # unremarkable substitute (same call spoken-extract's own doc makes).
    text = text.replace("—", ", ")
    # Strip emoji (crude but sufficient: anything outside common ranges
    # that isn't ASCII punctuation/letters/digits/whitespace).
    text = re.sub(
        r"[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]",
        "",
        text,
    )
    # Collapse whitespace.
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def load_front_digest_text(digest_date):
    path = DIGESTS_DIR / f"{digest_date}-front.md"
    if not path.exists():
        sys.exit(f"no front digest at {path}")
    raw = path.read_text()
    cleaned = clean_for_speech(raw)
    if not cleaned:
        sys.exit(f"front digest at {path} produced no speakable text after cleaning")
    return cleaned


def synthesize(text, wav_path):
    from kokoro import KPipeline
    import soundfile as sf
    import numpy as np

    pipeline = KPipeline(lang_code="a")
    chunks = []
    for _, _, audio in pipeline(text, voice="af_heart"):
        chunks.append(audio)
    if not chunks:
        sys.exit("kokoro produced no audio chunks")
    full = np.concatenate([c.numpy() if hasattr(c, "numpy") else c for c in chunks])
    sf.write(str(wav_path), full, 24000)


def wav_to_mp3(wav_path, mp3_path):
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error",
            "-i", str(wav_path),
            "-codec:a", "libmp3lame", "-qscale:a", "4",
            str(mp3_path),
        ],
        check=True,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("--out", default=str(DEFAULT_OUT_DIR))
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    text = load_front_digest_text(args.date)
    print(f"cleaned text: {len(text)} chars")

    wav_path = out_dir / f"{args.date}-front.wav"
    mp3_path = out_dir / f"{args.date}-front.mp3"

    synthesize(text, wav_path)
    print(f"wrote {wav_path} ({wav_path.stat().st_size} bytes)")

    wav_to_mp3(wav_path, mp3_path)
    wav_path.unlink()  # intermediate only — mp3 is the artifact
    print(f"wrote {mp3_path} ({mp3_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
