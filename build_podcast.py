#!/usr/bin/env python3
"""Build podcast MP3 from podcast_script.md using edge-tts + ffmpeg."""
import asyncio
import re
import subprocess
import sys
from pathlib import Path

import edge_tts

ROOT = Path(__file__).parent
SCRIPT = ROOT / "podcast_script.md"
OUT_DIR = ROOT / "podcast_parts"
FINAL = ROOT / "podcast.mp3"

FEMALE = "ru-RU-SvetlanaNeural"
MALE = "ru-RU-DmitryNeural"

LINE_RE = re.compile(r"^\*\*(А|Б):\*\*\s*(.+)$")


def parse_script(text: str):
    segments = []
    for line in text.splitlines():
        line = line.strip()
        m = LINE_RE.match(line)
        if not m:
            continue
        speaker, content = m.group(1), m.group(2).strip()
        voice = FEMALE if speaker == "А" else MALE
        segments.append((voice, content))
    return segments


async def synth(voice: str, text: str, out_path: Path):
    communicate = edge_tts.Communicate(text, voice, rate="+0%", pitch="+0Hz")
    await communicate.save(str(out_path))


async def main():
    OUT_DIR.mkdir(exist_ok=True)
    for old in OUT_DIR.glob("*.mp3"):
        old.unlink()

    segments = parse_script(SCRIPT.read_text(encoding="utf-8"))
    print(f"Segments: {len(segments)}")

    parts = []
    for idx, (voice, text) in enumerate(segments):
        out = OUT_DIR / f"{idx:03d}.mp3"
        print(f"[{idx+1}/{len(segments)}] {voice.split('-')[-1]}: {text[:60]}...")
        await synth(voice, text, out)
        parts.append(out)

    list_path = OUT_DIR / "list.txt"
    list_path.write_text("\n".join(f"file '{p.resolve()}'" for p in parts))

    cmd = [
        str(Path.home() / ".local/bin/ffmpeg"),
        "-y", "-f", "concat", "-safe", "0",
        "-i", str(list_path),
        "-c", "copy", str(FINAL),
    ]
    print("Concatenating...")
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"Done: {FINAL} ({FINAL.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    asyncio.run(main())
