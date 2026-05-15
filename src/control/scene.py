from control.sequences import Sequences
from rig.light_array import LightArray
from rig.palette import Palette


class Scene:

    def __init__(self) -> None:
        array = LightArray()
        array.start()
        self.p = Palette()
        self.s = Sequences(array, self.p)

    async def exceute(self) -> None:
        # await self.s.all_shuffle_by_color_group(2)
        # await self.s.all_shuffle(self.p.BLUE.rgb, 2)
        # await self.s.all_flash_by_color_group(2)
        # await self.s.all_flash(self.p.BLUE.rgb, 10)
        # await self.s.chase(self.p.BLUE.rgb, 2)
        # await self.s.zone_single_activate_low_high(2, .25)
        # await self.s.zone_single_activate_high_low(2, .25)
        await self.s.zone_single_activate_random(3, 0.1)
        await self.s.all_off()
