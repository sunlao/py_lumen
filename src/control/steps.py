from asyncio import create_task
from patterns.fixture import Pattern
from rig.palette import Palette
from rig.rack import Rack


class Steps:

    def __init__(self) -> None:
        self.palette = Palette
        self.pattern = Pattern()
        self.rack = Rack()
        self.fixtures = self.rack.RINGS.fixtures

    async def all_off(self) -> None:
        off = self.palette.OFF.rgb
        tasks = [create_task(self.pattern.activate(f, off)) for f in self.fixtures]
        for t in tasks:
            await t

    async def all_shuffle_by_color_group(self) -> None:
        off = self.palette.OFF.rgb
        c = self.palette.COLORS
        big = self.rack.BIG
        small = [self.rack.SMF, self.rack.SMB]
        t1 = create_task(self.pattern.shuffle_by_cologroup(big, c, 0.0275))
        tl = [create_task(self.pattern.shuffle_by_cologroup(f, c, 0.375)) for f in small]
        tl.append(t1)
        for t in tl:
            await t

