from asyncio import sleep
from random import shuffle
from rpi_ws281x import Color
from models.colors import RGB, ColorGroup
from models.fixtures import Fixture
from rig.light_array import LightArray
from rig.palette import Palette


class Pattern:

    def __init__(self) -> None:
        p = Palette
        self.off = p.OFF.rgb
        self.array = LightArray()
        self.array.start()

    async def activate(self, fixture: Fixture, rgb: RGB):
        async with fixture.lock:
            for led in range(fixture.leds.start, fixture.leds.stop):
                self.array.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
            self.array.strip.show()

    async def chase(self, fixture: Fixture, rgb: RGB, delay: float):
        async with fixture.lock:
            for led in range(fixture.leds.start, fixture.leds.stop):
                self.array.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                self.array.strip.show()
                await sleep(delay)

    async def chase_multi(self, fixture: Fixture, colors: ColorGroup, loop_cnt: int, delay: float) -> None:
        leds = [l for l in range(fixture.leds.start, fixture.leds.stop)]
        palette = [c for c in colors.collection]
        spacing = (len(leds) // len(colors.collection)) * .5
        for _ in range(loop_cnt):
            chasers = [{"position": 0, "color": palette[0]}]
            for lead_step in range(len(leds)):
                if lead_step > 0 and lead_step % spacing == 0:
                    color = palette[len(chasers) % len(palette)]
                    chasers.append({"position": 0, "color": color})
                for chaser in chasers:
                    rgb = chaser["color"].rgb
                    led = leds[chaser["position"]]
                    self.array.strip.setPixelColor(
                        led,
                        Color(rgb.red, rgb.green, rgb.blue),
                    )
                    chaser["position"] = (chaser["position"] + 1) % len(leds)
                self.array.strip.show()
                await sleep(delay)

    async def flash(self, fixture: Fixture, rgb: RGB, delay: float):
        async with fixture.lock:
            for led in range(fixture.leds.start, fixture.leds.stop):
                self.array.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
            self.array.strip.show()
            await sleep(delay)
            for led in range(fixture.leds.start, fixture.leds.stop):
                self.array.strip.setPixelColor(
                    led, Color(self.off.red, self.off.green, self.off.blue)
                )
            self.array.strip.show()

    async def flash_by_cologroup(
        self, fixture: Fixture, colors: ColorGroup, delay: float
    ):
        async with fixture.lock:
            for c in colors.collection:
                for led in range(fixture.leds.start, fixture.leds.stop):
                    self.array.strip.setPixelColor(
                        led, Color(c.rgb.red, c.rgb.green, c.rgb.blue)
                    )
                self.array.strip.show()
                await sleep(delay)
                for led in range(fixture.leds.start, fixture.leds.stop):
                    self.array.strip.setPixelColor(
                        led, Color(self.off.red, self.off.green, self.off.blue)
                    )
                self.array.strip.show()

    async def shuffle(self, fixture: Fixture, rgb: RGB, delay: float):
        async with fixture.lock:
            leds = [l for l in range(fixture.leds.start, fixture.leds.stop)]
            shuffle(leds)
            for led in leds:
                self.array.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                self.array.strip.show()
                await sleep(delay)

    async def shuffle_by_cologroup(
        self, fixture: Fixture, colors: ColorGroup, delay: float
    ):
        async with fixture.lock:
            leds = [l for l in range(fixture.leds.start, fixture.leds.stop)]
            shuffle(leds)
            for led in leds:
                rgbs = [c.rgb for c in colors.collection]
                shuffle(rgbs)
                rgb = rgbs[0]
                self.array.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                self.array.strip.show()
                await sleep(delay)
