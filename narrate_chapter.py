import asyncio
import edge_tts
import os
import sys

def parse_segments_with_intro_outro(intro_file, story_file, outro_file):
    def parse_file(path):
        segments = []
        voice = None
        text = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    if voice and text:
                        segments.append((voice, " ".join(text)))
                        text = []
                    voice = line.strip("[]")
                elif line:
                    text.append(line)
            if voice and text:
                segments.append((voice, " ".join(text)))
        return segments

    return (
        parse_file(intro_file) +
        parse_file(story_file) +
        parse_file(outro_file)
    )

async def generate_audio(segments, chapter_name):
    os.makedirs(f"output/{chapter_name}", exist_ok=True)
    for i, (voice, text) in enumerate(segments, 1):
        file = f"output/{chapter_name}/segment_{i}.mp3"
        communicate = edge_tts.Communicate(text=text, voice=voice)
        await communicate.save(file)
        print(f"🎙️ Segment {i} saved using {voice}")

async def main():
    if len(sys.argv) < 2:
        print("❗ Usage: python narrate_chapter.py chapters/ramayana_ch2.txt")
        return

    story_path = sys.argv[1]
    chapter = os.path.splitext(os.path.basename(story_path))[0]
    segments = parse_segments_with_intro_outro("intros/intro.txt", story_path, "intros/outro.txt")
    await generate_audio(segments, chapter)

asyncio.run(main())
