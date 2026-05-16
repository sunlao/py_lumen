from control.sequences import Sequences
from models.colors import ColorGroup
from rig.light_array import LightArray
from rig.palette import Palette


class Scene:

    def __init__(self) -> None:
        array = LightArray()
        array.start()
        self.palette = Palette()
        self.colors = self.palette.COLORS
        self.s = Sequences(array, self.palette)

    def _colors_top3(self) -> ColorGroup:
        return ColorGroup(
            collection=tuple(
                c
                for c in self.colors.collection
                if c in (self.palette.PURPLE, self.palette.RED, self.palette.BLUE)
            )
        )

    async def execute(self) -> None:
        await self.s.all_shuffle_by_color_group(self.colors, 2)
        await self.s.all_shuffle(self.palette.PURPLE.rgb, 2)
        await self.s.all_flash_by_color_group(self.colors, 2)
        await self.s.all_flash(self.palette.RED.rgb, 10)
        await self.s.chase(self.palette.BLUE.rgb, self.colors, 2)
        await self.s.zone_single_activate_low_high(self.colors, 2, 0.25)
        await self.s.zone_single_activate_high_low(self.colors, 2, 0.25)
        await self.s.zone_single_activate_random(self.colors, 3, 0.1)
        await self.s.zone_three_activate_low_high(self._colors_top3(), 3, 0.5)
        await self.s.zone_three_activate_high_low(self._colors_top3(), 3, 0.5)
        await self.s.gobo_winking_eye(self.palette.PURPLE.rgb, 8, 0.5)
        await self.s.all_off()
