from asyncio import sleep
from rpi_ws281x import Color
from models.colors import FrameColorSets
from models.fixtures import Fixture, Frame


class GoboPattern:

    def __init__(self, light_array, palette) -> None:
        p = palette
        self.off = p.OFF.rgb
        self.array = light_array

    async def activate_frame(
        self, fixture: Fixture, frame: Frame, frame_color_sets: FrameColorSets, delay: float
    ) -> None:
        frame_color_set = next(f for f in frame_color_sets.frame_color_sets if f.name == frame.name)
        color_map = {c.ordinal: c.rgb for c in frame_color_set.color_maps}        
        async with fixture.lock:
            for color_set in frame.color_sets:
                for led in color_set.leds:
                    rgb = color_map[color_set.ordinal]
                    self.array.strip.setPixelColor(
                        led,
                        Color(rgb.red, rgb.green, rgb.blue),
                    )
            self.array.strip.show()
            await sleep(delay)
