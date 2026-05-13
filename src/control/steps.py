from asyncio import create_task
from patterns.fixture import Pattern
from rig.rack import Rack
from palette import Palette


class Steps:

    def __init__(self) -> None:
        self.palette = Palette
        self.pattern = Pattern()
        self.rack = Rack()
        self.fixtures = self.rack.RINGS.fixtures

    async def all_off(self) -> None:
        rgb = self.palette.OFF.rgb
        tasks = [create_task(self.pattern.activate(f, rgb)) for f in self.fixtures]
        for t in tasks:
            await t

    async def all_offshuffle_by_cologroup(self) -> None:
        c = self.palette.COLORS
        tasks = [
            create_task(self.pattern.shuffle_by_cologroup(f, c, 0.15))
            for f in self.fixtures
        ]
        for t in tasks:
            await t
