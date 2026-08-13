#!/usr/bin/env python3
"""Generate a daily audio briefing (mp3) from the front-page digest.

    python3 sources/generate_audio_briefing.py [--date YYYY-MM-DD] [--out DIR]

WHY THIS FILE EXISTS (2026-08-13). Ben asked for a daily audio briefing,
starting with the front/general feed. Two paths exist side by side on the
site: a zero-generation "Listen" button (theprojection-site's listen.js,
browser speechSynthesis, no file produced) and this — a real mp3, narrated
once a day in a fixed voice, for anyone who wants better quality than
whatever TTS engine their own device happens to ship.

ENGINE HISTORY: shipped first with self-hosted Kokoro TTS (free, ran
locally). Ben's verdict after hearing it: "sounds TERRIBLE." Replaced
same-day with the Gemini API's native TTS (`gemini-2.5-flash-preview-tts`)
— independently reviewed as sounding "crisp, clear, incredibly natural"
and the only one of the three real options researched (the others were
Google Cloud TTS's Chirp3-HD and Azure Neural TTS, both viable fallbacks
if this one ever proves unstable) that Google explicitly builds for this
exact job — long-form narration, podcast/audiobook style — rather than
general-purpose or conversational use. Tested end-to-end at full briefing
length (3,323 chars / ~3m10s of audio, one API call, no truncation or
errors) before being adopted as the default, specifically because
Google's own docs warn of quality drift on outputs "longer than a few
minutes" and this use case sits close to that boundary.

Known risk, accepted deliberately: the model is still Preview, not GA —
Google can change or deprecate it with less notice than a stable product.
If it ever breaks or degrades, Chirp3-HD (`google-cloud-texttospeech`,
GA, marketed for "news reading and broadcast content") is the researched
fallback — not built here, since the Gemini path works today and building
a second full path preemptively would be speculative engineering against
a problem that hasn't happened. Kokoro's code is not kept as a fallback:
its output is exactly the thing this switch was made to get away from,
so silently falling back to it on a Gemini outage would be worse than
just skipping the day's audio (which is what happens now — see
publish/adapter.py's stage_audio_briefing(), which treats any failure
here as non-fatal to the rest of the publish run).

WHAT THIS NEEDS TO RUN (not yet baked into a shared image, so document it
here rather than let it go tribal):
  - A `GEMINI_API_KEY` env var (this repo's own `.env` — same var name
    `tools/publish.py` already loads instance `.env` files by convention).
    A Google AI Studio key (aistudio.google.com/apikey), not a bare GCP
    Console credential — the latter needs the Generative Language API
    explicitly enabled and isn't the same issuance flow. Confirmed the
    hard way: an initial key failed with API_KEY_INVALID; regenerating
    via AI Studio directly fixed it immediately.
  - A Python venv with `google-genai` installed — see
    /workspace/.venvs/kokoro-tts (name is a holdover from the Kokoro era;
    NOT inside any git repo, this is local build tooling, not instance
    data, same reasoning as gitignoring artifacts/read/ derived output).
    Reused rather than renamed since it already has the wav/mp3 tooling
    this script also needs (soundfile no longer required by this path,
    but ffmpeg still is).
  - System `ffmpeg`, for the wav -> mp3 conversion at the end (the Gemini
    API returns raw PCM, not an already-encoded file).

Run it with:
    /workspace/.venvs/kokoro-tts/bin/python3 sources/generate_audio_briefing.py

WHAT IT DOES: reads the given day's front digest
(artifacts/digests/daily/<date>-front.md), strips it down to clean speakable
prose (deliberately the same category of cleanup as ~/bin/spoken-extract's
clean_for_speech() — strip markdown/headers/links/emoji, keep plain
sentences — this is a second, independent implementation, not a shared
import, since spoken-extract lives on a different machine entirely and
narrates live chat, not a file), synthesizes it via the Gemini API in one
call (voice "Kore"), and writes an mp3 to the given output directory
(default: this repo's own artifacts/audio/, from which publish/adapter.py's
stage_audio_briefing() copies it into theprojection-site's static/ as
part of every normal `/daily` publish pass — see that function for the
automatic-generation wiring; this script is the piece it shells out to).
"""

import argparse
import os
import re
import subprocess
import sys
import wave
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIGESTS_DIR = REPO_ROOT / "artifacts" / "digests" / "daily"
DEFAULT_OUT_DIR = REPO_ROOT / "artifacts" / "audio"

GEMINI_TTS_MODEL = "gemini-2.5-flash-preview-tts"
GEMINI_TTS_VOICE = "Kore"

_MONTH_NAMES = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def _spoken_date(month, day, year=None):
    """(8, 13, '2026') -> 'August 13, 2026'; (8, 13) -> 'August 13'.
    Falls back to returning None (caller keeps the original text) for
    anything outside a real calendar date, so a coincidental MM-DD-shaped
    number is never silently mangled."""
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return None
    spoken = f"{_MONTH_NAMES[month - 1]} {day}"
    return f"{spoken}, {year}" if year else spoken


def clean_for_speech(text):
    """Markdown -> plain speakable prose. Independent of, but the same
    category of cleanup as, ~/bin/spoken-extract's clean_for_speech()."""
    # Dates -> spoken form (2026-08-13 real listen-test finding: Gemini TTS
    # read "08-13" as "oh-eight thirteen" rather than "August 13th" — minor,
    # but a plain giveaway of machine-read text a human wouldn't produce).
    # Full ISO dates first (they're everywhere in this repo's own dated
    # references, e.g. "resolved 2026-08-05"), then this repo's own bare
    # MM-DD shorthand for cross-referencing other digest-days (e.g. "since
    # 08-10") once the four-digit-year form can no longer swallow them.
    text = re.sub(
        r"\b(\d{4})-(\d{2})-(\d{2})\b",
        lambda m: _spoken_date(int(m.group(2)), int(m.group(3)), m.group(1)) or m.group(0),
        text,
    )
    text = re.sub(
        r"\b(0[1-9]|1[0-2])-([0-3]\d)\b",
        lambda m: _spoken_date(int(m.group(1)), int(m.group(2))) or m.group(0),
        text,
    )
    # Drop YAML frontmatter.
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    # Drop fenced code blocks and inline code markers (keep the content).
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = text.replace("`", "")
    # Drop the italic "*Curated from ...*" methodology/provenance line every
    # digest opens with (2026-08-13, real listen-test finding: it was the
    # FIRST thing spoken — "curated from four lenses, pipeline plus
    # agentic-interim WebFetch verification, collection window..." — dry
    # collection metadata nobody wants read aloud, and a genuinely bad
    # first impression regardless of voice quality. It's always the first
    # italic block right after the title, so remove it before the generic
    # bold/italic stripping below would otherwise just de-markup it in place.
    text = re.sub(r"^\*Curated from.*?\*\s*\n", "", text, flags=re.DOTALL | re.MULTILINE)
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
    text = text.strip()
    # Mark paragraph breaks with an explicit pause cue (2026-08-13, real
    # listen-test finding: without this, a Gemini-listens-to-itself check
    # described the read as jumping between wholly unrelated topics -
    # Anthropic corporate news, Iran/Hormuz, a crime story, state
    # legislation - "without meaningful pauses or shift in vocal tone." A
    # blank line alone wasn't enough signal. Re-verified via the same
    # listening check that this marker gets HONORED as a pause, not read
    # aloud as literal text - if that behavior ever changes on Google's
    # side, that's the first thing to re-test before trusting this output.
    text = re.sub(r"\n\n", ' <break time="700ms"/> ', text)
    return text


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
    from google import genai
    from google.genai import types

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("GEMINI_API_KEY not set — see this script's own docstring")

    client = genai.Client(api_key=api_key)
    style_instruction = (
        "Read this news briefing the way an experienced broadcast journalist "
        "reads a morning news roundup: warm and conversational, not rushed. "
        "Take a real, natural breath and a genuine beat between separate "
        "stories, especially where the subject changes completely (finance "
        "to geopolitics to a local crime story, for example) — do not "
        "barrel from one topic straight into the next at the same flat "
        "pace. Vary your pacing and emphasis based on what actually "
        "matters in each sentence, the way a person telling someone real "
        "news would, not a machine reading text top to bottom. Text marked "
        "<break time=\"700ms\"/> is a paragraph boundary — pause there "
        "audibly rather than reading the marker itself. Now read: "
    )
    response = client.models.generate_content(
        model=GEMINI_TTS_MODEL,
        contents=style_instruction + text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=GEMINI_TTS_VOICE
                    )
                )
            ),
        ),
    )
    audio_bytes = response.candidates[0].content.parts[0].inline_data.data
    if not audio_bytes:
        sys.exit("Gemini TTS returned no audio data")

    # The API returns raw 24kHz/16-bit/mono PCM, not an encoded file.
    with wave.open(str(wav_path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(audio_bytes)


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
