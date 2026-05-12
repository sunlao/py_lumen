from models.colors import RGB, ColorGroup
from control.light_rig import LightRig
from control.sequencer import Sequencer
from models.fixtures import Fixture


class Pattern:

    def __init__(self) -> None:
        s = Sequencer
        self.off = s.OFF.rgb
        self.rig = LightRig()
        self.rig.start()
        self.rack = self.rig.FIXTURES.rack

    async def activate(self, fixture: Fixture, rgb: RGB):
        async with fixture.lock:
            for led in range(fixture.leds.start, fixture.leds.stop):
                self.rig.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
            self.rig.strip.show()

    async def chase(self, fixture: Fixture, rgb: RGB, delay: float):
        async with fixture.lock:
            for led in range(fixture.leds.start, fixture.leds.stop):
                self.rig.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                self.rig.strip.show()
                await sleep(delay)

    async def flash(self, fixture: Fixture, rgb: RGB, delay: float):
        async with fixture.lock:
            for led in range(fixture.leds.start, fixture.leds.stop):
                self.rig.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
            self.rig.strip.show()
            for led in range(fixture.leds.start, fixture.leds.stop):
                self.rig.strip.setPixelColor(
                    led, Color(self.off.red, self.off.green, self.off.blue)
                )
            self.rig.strip.show()

    async def flash_by_cologroup(
        self, fixture: Fixture, colors: ColorGroup, delay: float
    ):
        async with fixture.lock:
            for led in range(fixture.leds.start, fixture.leds.stop):
                self.rig.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
            self.rig.strip.show()
            await sleep(delay)
            for led in range(fixture.leds.start, fixture.leds.stop):
                self.rig.strip.setPixelColor(
                    led, Color(self.off.red, self.off.green, self.off.blue)
                )
            self.rig.strip.show()

    async def shuffle(self, fixture: Fixture, rgb: RGB, delay: float):
        async with fixture.lock:
            leds = [l for l in range(fixture.leds.start, fixture.leds.stop)]
            shuffle(leds)
            for led in leds:
                self.rig.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                self.rig.strip.show()
                await sleep(delay)

    async def shuffle_by_cologroup(
        self, fixture: Fixture, colors: ColorGroup, delay: float
    ):
        async with fixture.lock:
            leds = [l for l in range(fixture.leds.start, fixture.leds.stop)]
            shuffle(leds)
            for led in leds:
                for c in colors:
                    self.rig.strip.setPixelColor(
                        led, Color(c.rgb.red, c.rgb.green, c.rgb.blue)
                    )
                    self.rig.strip.show()
                    await sleep(delay)
