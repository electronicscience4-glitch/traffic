import asyncio
from machine import Pin

red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

async def traffic_light():
    while True:
        # سەوز بۆ ٣ چرکە
        green.value(1)
        await asyncio.sleep(3)
        green.value(0)
        
        # زەرد بۆ ١ چرکە
        yellow.value(1)
        await asyncio.sleep(1)
        yellow.value(0)
        
        # سوور بۆ ٣ چرکە
        red.value(1)
        await asyncio.sleep(3)
        red.value(0)

asyncio.run(traffic_light())