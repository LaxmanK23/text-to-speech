import asyncio
import edge_tts
import os
import sys

def parse_bilingual_story(file_path):
    segments = []
    current_voice = None
    current_text = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                if current_voice and current_text:
                    segments.append((current_voice, " ".join(current_text)))
                    current_text = []
                current_voice = line.strip("[]")
            elif line:
                current_text.append(line)
        if current_voice and current_text:
            segments.append((current_voice, " ".join(current_text)))
    return segments

async def generate_audio(segments, chapter_name):
    segment_count = 1
    os.makedirs(f"output/{chapter_name}", exist_ok=True)

    for voice, text in segments:
        filename = f"output/{chapter_name}/segment_{segment_count}.mp3"
        communicate = edge_tts.Communicate(text=text, voice=voice)
        await communicate.save(filename)
        print(f"🎙️ Saved segment {segment_count} — {voice}")
        segment_count += 1

async def main():
    if len(sys.argv) < 2:
        print("❗ Usage: python narrate_chapter.py ramayana_ch2.txt")
        return

    chapter_file = sys.argv[1]
    chapter_name = os.path.splitext(os.path.basename(chapter_file))[0]
    segments = parse_bilingual_story(chapter_file)
    await generate_audio(segments, chapter_name)
    print(f"✅ All segments for {chapter_name} generated.")

asyncio.run(main())
