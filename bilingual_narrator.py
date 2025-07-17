import asyncio
import edge_tts
import os

input_file = "ramayana_ch1.txt"

# Parse the story into segments: (voice_name, text)
def parse_bilingual_story(file_path):
    segments = []
    current_voice = None
    current_text = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                # Save previous segment
                if current_voice and current_text:
                    segments.append((current_voice, " ".join(current_text)))
                    current_text = []
                current_voice = line.strip("[]")
            elif line:
                current_text.append(line)

        # Append final segment
        if current_voice and current_text:
            segments.append((current_voice, " ".join(current_text)))

    return segments

# Narrate and save segments
async def create_narration(segments):
    combined_audio = b""
    segment_count = 1

    for voice, text in segments:
        filename = f"segment_{segment_count}.mp3"
        communicate = edge_tts.Communicate(text=text, voice=voice)
        await communicate.save(filename)
        print(f"🎙️ Saved segment {segment_count} with voice: {voice}")
        segment_count += 1

async def main():
    segments = parse_bilingual_story(input_file)
    await create_narration(segments)
    print("✅ All segments generated! You can now mix them with music.")

asyncio.run(main())
