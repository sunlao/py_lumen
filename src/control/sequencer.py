from random import shuffle
from asyncio import sleep, create_task
from collections.abc import Awaitable, Callable
from rpi_ws281x import Color as Color
from models.colors import Colors, RGB, ColorGroup
from models.fixtures import Fixture
from control.light_rig import LightRig
from patterns.fixture import Pattern


class Sequencer:

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
    COLORS = ColorGroup(
        collection=(PURPLE, RED, CYAN, GREEN, YELLOW, ORANGE, PINK, BLUE)
    )

    def __init__(self) -> None:
        self.pattern = Pattern()
        self.rig = LightRig()
        self.rig.start()
        self.rack = self.rig.FIXTURES.rack

    async def all_red_activate(self):
        tasks = [create_task(self.pattern.activate(f, self.RED.rgb)) for f in self.rack]
        for t in tasks:
            await t
        await sleep(2)
        tasks = [create_task(self._activate_all(f, self.OFF.rgb)) for f in self.rack]
        for t in tasks:
            await t

    async def all_blue_random(self):
        tasks = [
            create_task(self.pattern.shuffle(f, self.BLUE.rgb, 0.1)) for f in self.rack
        ]
        for t in tasks:
            await t
        await sleep(2)
        tasks = [create_task(self._activate_all(f, self.OFF.rgb)) for f in self.rack]
        for t in tasks:
            await t
