from control.sequences import Sequences
from rig.palette import Palette


class Scene:

    def __init__(self) -> None:
        self.s = Sequences()
        self.p = Palette()

    async def exceute(self) -> None:
        await self.s.all_shuffle_by_color_group(2)
        await self.s.all_shuffle(self.p.BLUE.rgb, 2)
        await self.s.all_flash_by_color_group(2)
        await self.s.all_flash(self.p.BLUE.rgb, 10)
        await self.s.chase(self.p.BLUE.rgb, 2)
