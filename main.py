import asyncio
import edge_tts

output_file = "molasses_flood_story.mp3"

# Plain text with simulated emotion
emotional_story = """
Have you ever heard of the day... a wave of molasses destroyed a city?

It sounds funny — even silly — but it's one of the strangest... and deadliest events in American history.

It was 1919. In Boston’s North End stood a massive steel tank — 50 feet tall, 90 feet wide — filled with over two million gallons of thick, sticky molasses.

Locals said it groaned... and leaked. But the company? They just painted it brown... to hide the drips.

Then one unusually warm January day... it happened.

The tank exploded.

A wall of molasses — 25 feet high — came roaring down the streets at 35 miles per hour.

Buildings were crushed. Trains derailed. People and horses... were drowned.

By the end... 21 people were dead. 150 injured. And the entire neighborhood? Coated in sticky, brown syrup.

And even today... they say... on hot days in Boston’s North End... you can still smell it.
"""

async def tts():
    communicate = edge_tts.Communicate(text=emotional_story, voice="en-IN-PrabhatNeural")
    await communicate.save(output_file)

asyncio.run(tts())
print(f"✅ Audio saved as {output_file}")
