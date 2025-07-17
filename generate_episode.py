import asyncio
import edge_tts
import os
import json
from pydub import AudioSegment

# Load config
with open("episode_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Helper: Parse [voice] + lines from a txt file
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
            else:
                text.append(line)
        if voice and text:
            segments.append((voice, " ".join(text)))
    return segments

# Async: Generate audio segments
async def generate_segments(all_segments):
    audio_files = []
    os.makedirs("temp_audio", exist_ok=True)
    for i, (voice, text) in enumerate(all_segments, 1):
        filename = f"temp_audio/segment_{i}.mp3"
        tts = edge_tts.Communicate(text=text, voice=voice)
        await tts.save(filename)
        audio_files.append(filename)
        print(f"✅ Generated: {filename} with voice {voice}")
    return audio_files

# Combine audio with silence & music
def mix_segments(audio_paths, background_path, output_path, silence_ms, fade_ms):
    final = AudioSegment.silent(duration=0)
    silence = AudioSegment.silent(duration=silence_ms)

    for i, path in enumerate(audio_paths):
        seg = AudioSegment.from_file(path)
        seg = seg.fade_in(fade_ms).fade_out(fade_ms)
        final += seg + silence

    if background_path and os.path.exists(background_path):
        bg = AudioSegment.from_file(background_path) - 20
        bg = bg * (len(final) // len(bg) + 1)
        bg = bg[:len(final)]
        final = bg.overlay(final)

    final.export(output_path, format="mp3")
    print(f"\n🎧 Final mix saved as: {output_path}")

# Main runner
async def run_episode_pipeline():
    intro = parse_file(config["intro_file"])
    story = parse_file(config["story_file"])
    outro = parse_file(config["outro_file"])
    all_segments = intro + story + outro

    segment_files = await generate_segments(all_segments)
    mix_segments(
        segment_files,
        background_path=config["background_music"],
        output_path=config["output_filename"],
        silence_ms=config["silence_between_segments_ms"],
        fade_ms=config["fade_duration_ms"]
    )

asyncio.run(run_episode_pipeline())
