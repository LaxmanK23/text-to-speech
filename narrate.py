import asyncio
import edge_tts

input_file = "story.txt"
output_audio = "narration.mp3"
voice = "hi-IN-SwaraNeural"


async def narrate_story():
    with open(input_file, "r", encoding="utf-8") as f:
        story_text = f.read()

    communicate = edge_tts.Communicate(text=story_text, voice=voice)
    await communicate.save(output_audio)
    print(f"✅ Narration saved as {output_audio}")

asyncio.run(narrate_story())
