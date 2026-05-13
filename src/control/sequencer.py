from random import shuffle
from asyncio import sleep, create_task
from collections.abc import Awaitable, Callable
from rpi_ws281x import Color as Color
from models.colors import Colors, RGB, ColorGroup
from models.fixtures import Fixture
from patterns.fixture import Pattern


class Sequencer:

    def __init__(self) -> None:
        self.pattern = Pattern()

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
        await sleep(1)
        tasks = [create_task(self._activate_all(f, self.OFF.rgb)) for f in self.rack]
        for t in tasks:
            await t
