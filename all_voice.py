import asyncio
import edge_tts

async def list_voices():
    voices = await edge_tts.list_voices()
    for v in voices:
        if "hi-IN" in v["ShortName"] or "en-IN" in v["ShortName"]:
            print(f"{v['ShortName']} — {v['Gender']} — {v['LocaleName']}")

asyncio.run(list_voices())
