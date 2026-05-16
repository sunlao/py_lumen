from asyncio import sleep
from rpi_ws281x import Color
from models.colors import RGB
from models.fixtures import Fixture, Zones, Frame


class GoboPattern:

    def __init__(self, light_array, palette) -> None:
        p = palette
        self.off = p.OFF.rgb
        self.array = light_array

    async def activate_frame(
        self, fixture: Fixture, frame: Frame, rgb: RGB, delay: float
    ) -> None:
        async with fixture.lock:
            for led in frame.leds:
                self.array.strip.setPixelColor(
                    led,
                    Color(rgb.red, rgb.green, rgb.blue),
                )
            self.array.strip.show()
            await sleep(delay)
