from asyncio import sleep
from random import shuffle
from rpi_ws281x import Color
from models.colors import RGB, ColorGroup
from models.fixtures import Zone
from rig.light_array import LightArray
from rig.palette import Palette


class Pattern:

    def __init__(self) -> None:
        p = Palette
        self.off = p.OFF.rgb
        self.array = LightArray()
        self.array.start()

    async def activate(self, zone: Zone, rgb: RGB):
        async with fixture.lock:
            for led in range(zone.start, zone.stop):
                self.array.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
            self.array.strip.show()

    async def chase(self, zone: Zone, rgb: RGB, delay: float):
        async with fixture.lock:
            for led in range(zone.start, zone.stop):
                self.array.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                self.array.strip.show()
                await sleep(delay)

    async def flash(self, zone: Zone, rgb: RGB, delay: float):
        async with fixture.lock:
            for led in range(zone.start, zone.stop):
                self.array.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
            self.array.strip.show()
            for led in range(zone.start, zone.stop):
                self.array.strip.setPixelColor(
                    led, Color(self.off.red, self.off.green, self.off.blue)
                )
            self.array.strip.show()

    async def flash_by_cologroup(self, zone: Zone, colors: ColorGroup, delay: float):
        async with fixture.lock:
            for led in range(zone.start, zone.stop):
                self.array.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
            self.array.strip.show()
            await sleep(delay)
            for led in range(zone.start, zone.stop):
                self.array.strip.setPixelColor(
                    led, Color(self.off.red, self.off.green, self.off.blue)
                )
            self.array.strip.show()

    async def shuffle(self, zone: Zone, rgb: RGB, delay: float):
        async with fixture.lock:
            leds = [l for l in range(zone.start, zone.stop)]
            shuffle(leds)
            for led in leds:
                self.array.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                self.array.strip.show()
                await sleep(delay)

    async def shuffle_by_cologroup(self, zone: Zone, colors: ColorGroup, delay: float):
        async with fixture.lock:
            leds = [l for l in range(zone.start, zone.stop)]
            shuffle(leds)
            for led in leds:
                for c in colors:
                    self.array.strip.setPixelColor(
                        led, Color(c.rgb.red, c.rgb.green, c.rgb.blue)
                    )
                    self.array.strip.show()
                    await sleep(delay)
