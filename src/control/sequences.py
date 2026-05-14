from asyncio import create_task
from models.colors import RGB
from models.fixtures import Fixture
from patterns.fixture import Pattern
from rig.palette import Palette
from rig.rack import Rack


class Sequences:

    def __init__(self) -> None:
        palette = Palette
        self.off = palette.OFF.rgb
        self.colors = palette.COLORS
        self.pattern = Pattern()
        rack = Rack()
        self.big = rack.BIG
        self.small = [rack.SMF, rack.SMB]
        self.fixtures = rack.RINGS.fixtures

    async def _small_chase(self, fixture: Fixture, rgb: RGB) -> None:
        await self.small_off()
        for _ in range(5):
            await self.pattern.chase(fixture, rgb, 0.1)
            await self.small_off()

    async def _big_chase(self) -> None:
        await self.pattern.activate(self.big, self.off)
        for _ in range(2):
            await self.pattern.chase_multi(self.big, self.colors, 0.01)

    async def all_off(self) -> None:
        tasks = [create_task(self.pattern.activate(f, self.off)) for f in self.fixtures]
        for t in tasks:
            await t

    async def all_flash(self, rgb: RGB, repeat) -> None:
        await self.all_off()
        for _ in range(repeat):
            tasks = [
                create_task(self.pattern.flash(f, rgb, 0.025)) for f in self.fixtures
            ]
            for t in tasks:
                await t

    async def all_flash_by_color_group(self, repeat) -> None:
        await self.all_off()
        for _ in range(repeat):
            tasks = [
                create_task(self.pattern.flash_by_cologroup(f, self.colors, 0.025))
                for f in self.fixtures
            ]
            for t in tasks:
                await t

    async def all_shuffle(self, rgb: RGB, repeat) -> None:
        await self.all_off()
        for _ in range(repeat):
            task = create_task(self.pattern.shuffle(self.big, rgb, 0.0275))
            tasks = [
                create_task(self.pattern.shuffle(f, rgb, 0.375)) for f in self.small
            ]
            tasks.append(task)
            for t in tasks:
                await t
            await self.all_off()

    async def all_shuffle_by_color_group(self, repeat) -> None:
        await self.all_off()
        for _ in range(repeat):
            task = create_task(
                self.pattern.shuffle_by_cologroup(self.big, self.colors, 0.0275)
            )
            tasks = [
                create_task(self.pattern.shuffle_by_cologroup(f, self.colors, 0.375))
                for f in self.small
            ]
            tasks.append(task)
            for t in tasks:
                await t
            await self.all_off()

    async def chase(self, rgb: RGB, repeat) -> None:
        for _ in range(repeat):
            task = create_task(self._big_chase())
            tasks = [create_task(self._small_chase(f, rgb)) for f in self.small]
            tasks.append(task)
            for t in tasks:
                await t
        await self.all_off()

    async def small_off(self) -> None:
        tasks = [create_task(self.pattern.activate(f, self.off)) for f in self.small]
        for t in tasks:
            await t
