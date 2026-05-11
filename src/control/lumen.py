from random import shuffle
from asyncio import Lock, sleep, create_task
from rpi_ws281x import Color, PixelStrip
from models.colors import Colors, RGB


class Lumen:

    OFF = Colors(name="OFF", ordinal=0, rgb=RGB(red=0, green=0, blue=0))
    WHITE = Colors(name="WHITE", ordinal=1, rgb=RGB(red=255, green=255, blue=255))
    PURPLE = Colors(name="PURPLE", ordinal=2, rgb=RGB(red=100, green=0, blue=175))
    RED = Colors(name="RED", ordinal=3, rgb=RGB(red=255, green=0, blue=0))
    CYAN = Colors(name="CYAN", ordinal=4, rgb=RGB(red=0, green=180, blue=220))
    GREEN = Colors(name="GREEN", ordinal=5, rgb=RGB(red=20, green=120, blue=20))
    YELLOW = Colors(name="YELLOW", ordinal=6, rgb=RGB(red=255, green=180, blue=0))
    ORANGE = Colors(name="ORANGE", ordinal=7, rgb=RGB(red=255, green=50, blue=0))
    PINK = Colors(name="PINK", ordinal=8, rgb=RGB(red=254, green=0, blue=150))
    BLUE = Colors(name="BLUE", ordinal=9, rgb=RGB(red=0, green=0, blue=255))
    COLORS = [OFF, WHITE, PURPLE, RED, CYAN, GREEN, YELLOW, ORANGE, PINK, BLUE]
    # COLORS = [OFF, WHITE, RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE]

    def __init__(self) -> None:
        pin = 10
        self.rings = {
            "small_f": {"leds": range(0, 24), "lock": Lock()},
            "small_b": {"leds": range(24, 48), "lock": Lock()},
            "big": {"leds": range(48, 289), "lock": Lock()},
        }

        self.ring_zones = {
            1: {"leds": range(48, 108)},  # 60
            2: {"leds": range(108, 156)},  # 48
            3: {"leds": range(156, 196)},  # 40
            4: {"leds": range(196, 228)},  # 32
            5: {"leds": range(228, 252)},  # 24
            6: {"leds": range(252, 268)},  # 16
            7: {"leds": range(268, 280)},  # 12
            8: {"leds": range(280, 288)},  # 8
            9: {"leds": range(288, 289)},  # 1
        }

        self.led_count = sum(len(ring["leds"]) for ring in self.rings.values())
        self.strip = PixelStrip(self.led_count, pin, brightness=30)

    def _next_color(self, ordinal):
        return None

    def all_off(self) -> None:
        rgb = self.OFF.rgb
        for led in range(self.led_count):
            self.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
        self.strip.show()

    async def color_on(self, ring: str, rgb: RGB) -> None:
        async with self.rings[ring]["lock"]:
            for led in self.rings[ring]["leds"]:
                self.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
            self.strip.show()

    async def shuffle_led(self, ring: str, rgb: RGB, delay: float) -> None:
        async with self.rings[ring]["lock"]:
            leds = list(self.rings[ring]["leds"])
            shuffle(leds)
            for led in leds:
                self.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                self.strip.show()
                await sleep(delay)

    async def shuffle_led_shuffle_color(self, ring: str, delay: float) -> None:
        async with self.rings[ring]["lock"]:
            leds = list(self.rings[ring]["leds"])
            shuffle(leds)
            for led in leds:
                colors = [c.rgb for c in self.COLORS if c.name not in ("OFF", "WHITE")]
                shuffle(colors)
                rgb = colors[0]
                self.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                self.strip.show()
                await sleep(delay)

    async def flash_random(self, ring: str, loop_cnt: int) -> None:
        async with self.rings[ring]["lock"]:
            leds = list(self.rings[ring]["leds"])
            colors = [c.rgb for c in self.COLORS if c.name not in ("OFF", "WHITE")]
            for _ in range(0, loop_cnt):
                for rgb in colors:
                    for led in leds:
                        self.strip.setPixelColor(
                            led, Color(rgb.red, rgb.green, rgb.blue)
                        )
                    self.strip.show()
                    await sleep(0.1)

    async def led_chase(self, ring: str, loop_cnt: int, speed: float) -> None:
        async with self.rings[ring]["lock"]:
            leds = list(self.rings[ring]["leds"])
            colors = [c.rgb for c in self.COLORS if c.name not in ("OFF", "WHITE")]
            for _ in range(0, loop_cnt):
                for rgb in colors:
                    for led in leds:
                        self.strip.setPixelColor(
                            led, Color(rgb.red, rgb.green, rgb.blue)
                        )
                        self.strip.show()
                        await sleep(speed)

    async def big_led_chase(self, loop_cnt: int, speed: float) -> None:
        async with self.rings["big"]["lock"]:
            leds = list(self.rings["big"]["leds"])
            colors = [c for c in self.COLORS if c.name not in ("OFF", "WHITE")]
            spacing = 15
            for _ in range(loop_cnt):
                chasers = [{"position": 0, "color": colors[0]}]
                for lead_step in range(len(leds)):
                    if lead_step > 0 and lead_step % spacing == 0:
                        color = colors[len(chasers) % len(colors)]
                        chasers.append({"position": 0, "color": color})
                    for chaser in chasers:
                        rgb = chaser["color"].rgb
                        led = leds[chaser["position"]]
                        self.strip.setPixelColor(
                            led, Color(rgb.red, rgb.green, rgb.blue)
                        )
                        chaser["position"] = (chaser["position"] + 1) % len(leds)
                    self.strip.show()
                    await sleep(speed)

    async def increment_zone(self) -> None:
        async with self.rings["big"]["lock"]:
            colors = [c for c in self.COLORS if c.name not in ("OFF", "WHITE")]
            first_pass = True
            for color in colors:
                rgb = color.rgb
                print(f"color.ordinal: {color.ordinal}")
                for zone in self.ring_zones:
                    if color.ordinal < 9:
                        next_rgb = [
                            c.rgb for c in colors if c.ordinal == color.ordinal + 1
                        ][0]
                    else:
                        next_rgb = [
                            c.rgb for c in colors if c.ordinal == color.ordinal - 7
                        ][0]
                    next_rgb2 = rgb
                    if color.ordinal < 8:
                        next_rgb2 = [
                            c.rgb for c in colors if c.ordinal == color.ordinal + 2
                        ][0]
                    else:
                        next_rgb2 = [
                            c.rgb for c in colors if c.ordinal == color.ordinal - 6
                        ][0]
                    print(f"zone: {zone}")
                    if first_pass is True:
                        for led in self.ring_zones[zone]["leds"]:
                            self.strip.setPixelColor(
                                led, Color(rgb.red, rgb.green, rgb.blue)
                            )
                        if zone >= 4:
                            for led in self.ring_zones[zone - 3]["leds"]:
                                self.strip.setPixelColor(
                                    led,
                                    Color(next_rgb.red, next_rgb.green, next_rgb.blue),
                                )
                        if zone >= 7:
                            for led in self.ring_zones[zone - 6]["leds"]:
                                self.strip.setPixelColor(
                                    led,
                                    Color(
                                        next_rgb2.red, next_rgb2.green, next_rgb2.blue
                                    ),
                                )
                    self.strip.show()
                    await sleep(1)
                    if first_pass is False:
                        for led in self.ring_zones[zone]["leds"]:
                            self.strip.setPixelColor(
                                led, Color(rgb.red, rgb.green, rgb.blue)
                            )
                        if zone >= 4:
                            for led in self.ring_zones[zone - 3]["leds"]:
                                self.strip.setPixelColor(
                                    led,
                                    Color(next_rgb.red, next_rgb.green, next_rgb.blue),
                                )
                        if zone >= 7:
                            for led in self.ring_zones[zone - 6]["leds"]:
                                self.strip.setPixelColor(
                                    led,
                                    Color(
                                        next_rgb2.red, next_rgb2.green, next_rgb2.blue
                                    ),
                                )

                    # next_rgb = rgb
                    # if color.ordinal < 9:
                    #     next_rgb = [c.rgb for c in colors if c.ordinal == color.ordinal + 1][0]
                    # if color.ordinal < 8:
                    #     next_rgb2 = [c.rgb for c in colors if c.ordinal == color.ordinal + 2][0]
                    # print(f"zone: {zone}")
                    # if zone < 4 and color.ordinal == 2:
                    #     for led in self.ring_zones[zone]["leds"]:
                    #         self.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                    # if zone >= 4 and zone < 9:
                    #     for led in self.ring_zones[zone]["leds"]:
                    #         self.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                    #     for led in self.ring_zones[zone - 3]["leds"]:
                    #         self.strip.setPixelColor(led, Color(next_rgb.red, next_rgb.green, next_rgb.blue))
                    # if zone >= 7 and zone < 9:
                    #     for led in self.ring_zones[zone - 6]["leds"]:
                    #         self.strip.setPixelColor(led, Color(next_rgb2.red, next_rgb2.green, next_rgb2.blue))

                    # rgb_next = rgb
                    # if color.ordinal < 9:
                    #     rgb_next = [c.rgb for c in colors if c.ordinal == color.ordinal + 1][0]
                    # if color.ordinal < :
                    #     rgb_next2 = [c.rgb for c in colors if c.ordinal == color.ordinal + 2][0]
                    # if color.ordinal == 2:
                    #     # ordinal 0 & 1 excluded by not in
                    #     # first pass only
                    #     for led in self.ring_zones[zone]["leds"]:
                    #         self.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                    # if zone >= 4 and color.ordinal != 9:
                    #     print(f"-next zone -1: {zone-3}")
                    #     for led in self.ring_zones[zone - 3]["leds"]:
                    #         self.strip.setPixelColor(led, Color(rgb_next.red, rgb_next.green, rgb_next.blue))
                    # if color.ordinal > 2 and zone < 4 :
                    #     for led in self.ring_zones[zone + 6]["leds"]:
                    #         self.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                    # if color.ordinal > 2 and color.ordinal != 9:
                    #     for led in self.ring_zones[zone]["leds"]:
                    #         self.strip.setPixelColor(led, Color(rgb_next.red, rgb_next.green, rgb_next.blue))

                    # if zone <= 4 and color.ordinal > 2:
                    #     for led in self.ring_zones[zone]["leds"]:
                    #         self.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                    # if zone > 4 and color.ordinal > 2:
                    #         self.strip.setPixelColor(led, Color(rgb.red, rgb.green, rgb.blue))
                    #     for led in self.ring_zones[zone]["leds"]:
                    #     rgb_prev = [c.rgb for c in colors if c.ordinal == color.ordinal - 1][0]
                    #     for led in self.ring_zones[zone-4]["leds"]:
                    #         self.strip.setPixelColor(led, Color(rgb_prev.red, rgb_prev.green, rgb_prev.blue))
                    # if zone > 4 and zone < 8 and color.ordinal < 9:
                    #     rgb_next = [c.rgb for c in colors if c.ordinal == color.ordinal + 1][0]
                    #     # for led in self.ring_zones[zone-4]["leds"]:
                    #         # self.strip.setPixelColor(led, Color(rgb_next.red, rgb_next.green, rgb_next.blue))

    async def start(self) -> None:
        self.strip.begin()
        self.all_off()
        task_bg = create_task(self.shuffle_led_shuffle_color("big", 0.05))
        await sleep(0.5)
        task_b = create_task(self.shuffle_led_shuffle_color("small_b", 0.25))
        await sleep(0.5)
        task_f = create_task(self.shuffle_led_shuffle_color("small_f", 0.10))
        await task_bg
        await task_b
        await task_f
        await sleep(2)
        await self.color_on("small_f", self.RED.rgb)
        await sleep(0.5)
        await self.color_on("small_b", self.PURPLE.rgb)
        await sleep(0.5)
        await self.color_on("big", self.ORANGE.rgb)
        await sleep(0.5)
        await self.color_on("small_f", self.OFF.rgb)
        await sleep(0.5)
        await self.color_on("small_b", self.OFF.rgb)
        await sleep(0.5)
        await self.color_on("big", self.OFF.rgb)
        await sleep(0.5)
        task_bg = create_task(self.shuffle_led("big", self.BLUE.rgb, 0.10))
        await sleep(0.5)
        task_b = create_task(self.shuffle_led("small_b", self.CYAN.rgb, 0.25))
        await sleep(0.5)
        task_f = create_task(self.shuffle_led("small_f", self.PINK.rgb, 0.10))
        await task_bg
        await task_b
        await task_f
        await sleep(2)
        task_b = create_task(self.flash_random("small_b", 3))
        task_f = create_task(self.flash_random("small_f", 3))
        task_bg = create_task(self.flash_random("big", 1))
        await task_b
        await task_f
        await task_bg
        await sleep(1)
        task_b = create_task(self.led_chase("small_b", 2, 0.25))
        task_f = create_task(self.led_chase("small_f", 2, 0.15))
        await self.big_led_chase(3, 0.1)
        await task_b
        await task_f
        await task_bg
        self.all_off()
