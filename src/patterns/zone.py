from asyncio import sleep
from random import choice
from rpi_ws281x import Color
from models.colors import RGB, ColorGroup
from models.fixtures import Fixture, Zones


class Pattern:

    def __init__(self, light_array, palette) -> None:
        p = palette
        self.off = p.OFF.rgb
        self.array = light_array

    @staticmethod
    def _random_rgb(colors: ColorGroup, previous: RGB) -> RGB:
        color = choice(colors.collection)
        while color.rgb == previous:
            color = choice(colors.collection)
        return color.rgb

    async def activate_zones(
        self, fixture: Fixture, zones: Zones, colors: ColorGroup, delay: float
    ) -> None:
        previous = None
        async with fixture.lock:
            for zone in zones:
                rgb = self._random_rgb(colors, previous)
                previous = rgb
                for led in range(zone.start, zone.stop):
                    self.array.strip.setPixelColor(
                        led,
                        Color(rgb.red, rgb.green, rgb.blue),
                    )
                self.array.strip.show()
                await sleep(delay)
