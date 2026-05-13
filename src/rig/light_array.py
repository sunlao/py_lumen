from rpi_ws281x import PixelStrip
from rig.rack import Rack


class LightArray:

    PIN = 10
    BRIGHTNESS = 30

    def __init__(self) -> None:
        r = Rack()
        self.max_led = max(r.leds.stop for r in r.RINGS.fixtures)
        self.strip = PixelStrip(self.max_led, self.PIN, brightness=self.BRIGHTNESS)

    def start(self) -> None:
        self.strip.begin()
