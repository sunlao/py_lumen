from asyncio import create_task, sleep
from random import shuffle
from models.colors import RGB, ColorGroup
from models.fixtures import Fixture
from patterns.fixture import FixturePattern
from patterns.zone import ZonePattern
from patterns.gobo import GoboPattern
from rig.rack import Rack


class Sequences:

    def __init__(self, light_array, palette) -> None:
        self.off = palette.OFF.rgb
        self.f_pattern = FixturePattern(light_array, palette)
        self.z_pattern = ZonePattern(light_array, palette)
        self.g_pattern = GoboPattern(light_array, palette)
        rack = Rack()
        self.big = rack.BIG
        self.small = [rack.SMF, rack.SMB]
        self.fixtures = rack.RINGS.fixtures

    async def _small_chase(self, fixture: Fixture, rgb: RGB) -> None:
        await self.small_off()
        for _ in range(5):
            await self.f_pattern.chase(fixture, rgb, 0.1)
            await self.small_off()

    async def _big_chase(self, colors: ColorGroup) -> None:
        await self.f_pattern.activate(self.big, self.off)
        for _ in range(2):
            await self.f_pattern.chase_multi(self.big, colors, 0.01)

    async def all_off(self) -> None:
        tasks = [
            create_task(self.f_pattern.activate(f, self.off)) for f in self.fixtures
        ]
        for t in tasks:
            await t

    async def all_flash(self, rgb: RGB, repeat) -> None:
        await self.all_off()
        for _ in range(repeat):
            tasks = [
                create_task(self.f_pattern.flash(f, rgb, 0.025)) for f in self.fixtures
            ]
            for t in tasks:
                await t

    async def all_flash_by_color_group(self, colors: ColorGroup, repeat) -> None:
        await self.all_off()
        for _ in range(repeat):
            tasks = [
                create_task(self.f_pattern.flash_by_cologroup(f, colors, 0.025))
                for f in self.fixtures
            ]
            for t in tasks:
                await t

    async def all_shuffle(self, rgb: RGB, repeat) -> None:
        await self.all_off()
        for _ in range(repeat):
            task = create_task(self.f_pattern.shuffle(self.big, rgb, 0.0275))
            tasks = [
                create_task(self.f_pattern.shuffle(f, rgb, 0.375)) for f in self.small
            ]
            tasks.append(task)
            for t in tasks:
                await t
            await self.all_off()

    async def all_shuffle_by_color_group(self, colors: ColorGroup, repeat) -> None:
        await self.all_off()
        for _ in range(repeat):
            task = create_task(
                self.f_pattern.shuffle_by_cologroup(self.big, colors, 0.0275)
            )
            tasks = [
                create_task(self.f_pattern.shuffle_by_cologroup(f, colors, 0.375))
                for f in self.small
            ]
            tasks.append(task)
            for t in tasks:
                await t
            await self.all_off()

    async def chase(self, rgb: RGB, colors: ColorGroup, repeat) -> None:
        for _ in range(repeat):
            task = create_task(self._big_chase(colors))
            tasks = [create_task(self._small_chase(f, rgb)) for f in self.small]
            tasks.append(task)
            for t in tasks:
                await t
        await self.all_off()

    async def small_off(self) -> None:
        tasks = [create_task(self.f_pattern.activate(f, self.off)) for f in self.small]
        for t in tasks:
            await t

    async def zone_single_activate_low_high(
        self, colors: ColorGroup, repeat, delay: float
    ) -> None:
        for _ in range(repeat):
            await self.f_pattern.activate(self.big, self.off)
            await sleep(delay)
            zones = next(z.group for z in self.big.leds.zones if z.name == "single")
            await self.z_pattern.activate_zones_shuffle_color(
                self.big, zones, colors, delay
            )

    async def zone_single_activate_high_low(
        self, colors: ColorGroup, repeat, delay: float
    ) -> None:
        for _ in range(repeat):
            await self.f_pattern.activate(self.big, self.off)
            await sleep(delay)
            zones = next(z.group for z in self.big.leds.zones if z.name == "single")
            zones = sorted(zones, key=lambda z: z.ordinal, reverse=True)
            await self.z_pattern.activate_zones_shuffle_color(
                self.big, zones, colors, delay
            )

    async def zone_single_activate_random(
        self, colors: ColorGroup, repeat: int, delay: float
    ) -> None:
        for _ in range(repeat):
            await self.f_pattern.activate(self.big, self.off)
            await sleep(delay)
            zones = list(
                next(z.group for z in self.big.leds.zones if z.name == "single")
            )
            shuffle(zones)
            await self.z_pattern.activate_zones_shuffle_color(
                self.big, zones, colors, delay
            )

    async def zone_three_activate_low_high(
        self, colors: ColorGroup, repeat, delay: float
    ) -> None:
        for _ in range(repeat):
            await self.f_pattern.activate(self.big, self.off)
            await sleep(delay)
            zones = next(z.group for z in self.big.leds.zones if z.name == "three")
            await self.z_pattern.activate_zones(self.big, zones, colors, delay)

    async def zone_three_activate_high_low(
        self, colors: ColorGroup, repeat, delay: float
    ) -> None:
        for _ in range(repeat):
            await self.f_pattern.activate(self.big, self.off)
            await sleep(delay)
            zones = next(z.group for z in self.big.leds.zones if z.name == "three")
            zones = sorted(zones, key=lambda z: z.ordinal, reverse=True)
            await self.z_pattern.activate_zones(self.big, zones, colors, delay)

    async def gobo_winking_eye(self, rgb: RGB, repeat, delay: float) -> None:
        eye = next(g for g in self.big.leds.gobos if g.name == "eye")
        await self.f_pattern.activate(self.big, self.off)
        for _ in range(repeat):
            for frame in eye.group:
                await self.g_pattern.activate_frame(self.big, frame, rgb, delay)
                await self.f_pattern.activate(self.big, self.off)
