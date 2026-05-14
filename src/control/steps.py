from asyncio import create_task
from models.colors import RGB
from patterns.fixture import Pattern
from rig.palette import Palette
from rig.rack import Rack


class Steps:

    def __init__(self) -> None:
        palette = Palette
        self.off = palette.OFF.rgb
        self.colors = palette.COLORS
        self.pattern = Pattern()
        rack = Rack()
        self.big = rack.BIG
        self.small = [rack.SMF, rack.SMB]
        self.fixtures = rack.RINGS.fixtures

    async def all_off(self) -> None:
        tasks = [create_task(self.pattern.activate(f, self.off)) for f in self.fixtures]
        for t in tasks:
            await t

    async def small_chase(self, rgb: RGB, repeat) -> None:
        await self.all_off()
        for i in range(repeat):
            tasks = [
                create_task(self.pattern.chase(f, rgb, 0.375))
                for f in self.small
            ]
            for t in tasks:
                await t
            await self.all_off()


    async def big_chase(self, repeat) -> None:
        await self.all_off()
        for i in range(repeat):
            tasks = [
                create_task(self.pattern.chase_multi(self.big, self.colors, 0.025))
                for f in self.small
            ]
            for t in tasks:
                await t
        await self.all_off()

    async def all_flash(self, rgb: RGB, repeat) -> None:
        await self.all_off()
        for i in range(repeat):
            tasks = [
                create_task(self.pattern.flash(f, rgb, 0.025))
                for f in self.fixtures
            ]
            for t in tasks:
                await t

    async def all_flash_by_color_group(self, repeat) -> None:
        await self.all_off()
        for i in range(repeat):
            tasks = [
                create_task(self.pattern.flash_by_cologroup(f, self.colors, 0.025))
                for f in self.fixtures
            ]
            for t in tasks:
                await t

    async def all_shuffle(self, rgb: RGB, repeat) -> None:
        await self.all_off()
        for i in range(repeat):
            task = create_task(
                self.pattern.shuffle(self.big, rgb, 0.0275)
            )
            tasks = [
                create_task(self.pattern.shuffle(f, rgb, 0.375))
                for f in self.small
            ]
            tasks.append(task)
            for t in tasks:
                await t
            await self.all_off()

    async def all_shuffle_by_color_group(self, repeat) -> None:
        await self.all_off()
        for i in range(repeat):
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
