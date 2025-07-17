import asyncio
import edge_tts

# Output filename
output_file = "molasses_flood_story.mp3"

# SSML story content
ssml_story = """
<speak version='1.0' xml:lang='en-US'>
    <voice name='en-US-GuyNeural'>
        <prosody rate='medium' pitch='+2st'>
            <s>Have you ever heard of the day a wave of molasses destroyed a city?</s>
            <break time='500ms'/>
            <s>It sounds funny — but it’s one of the strangest and deadliest events in American history.</s>
            <break time='800ms'/>
            <s>It was 1919. A giant tank of molasses — fifty feet tall, ninety feet wide — stood in Boston’s North End.</s>
            <s>It held more than 2 million gallons of thick, sticky molasses.</s>
            <break time='600ms'/>
            <prosody rate='slow' pitch='-1st'>
                <s>Locals said the tank groaned and leaked.</s>
            </prosody>
            <break time='300ms'/>
            <s>But the company? They just painted it brown to hide the drips.</s>
            <break time='800ms'/>
            <prosody pitch='+1st'>
                <s>Then, one unusually warm January day...</s>
            </prosody>
            <s>...the tank exploded.</s>
            <break time='500ms'/>
            <prosody rate='fast' pitch='+3st'>
                <s>A wall of molasses — 25 feet high — raced down the street at 35 miles per hour!</s>
            </prosody>
            <s>It crushed buildings, derailed trains, and even drowned people and horses in its wake.</s>
            <break time='1s'/>
            <prosody rate='medium' pitch='0st'>
                <s>In the aftermath, 21 people were dead, 150 injured. Everything was covered in a sticky mess.</s>
                <s>And for weeks, the smell of molasses hung in the air.</s>
            </prosody>
            <break time='1s'/>
            <prosody rate='slow' pitch='-1st'>
                <s>To this day, they say that on hot days... you can still smell it in the North End.</s>
            </prosody>
        </prosody>
    </voice>
</speak>
"""

# Async TTS conversion
async def tts():
    communicate = edge_tts.Communicate(text=ssml_story, voice="en-US-GuyNeural")
    await communicate.save(output_file)

# Run the async function
asyncio.run(tts())

print(f"✅ Audio saved as {output_file}")
