from asyncio import run
from time import sleep
from control.steps import Steps
from rig.palette import Palette

p = Palette
s = Steps()



# run(s.all_shuffle_by_color_group(2))
# run(s.all_shuffle(p.BLUE.rgb, 2))
# run(s.all_flash_by_color_group(2))
# run(s.all_flash(p.BLUE.rgb, 10))
# run(s.small_chase(p.BLUE.rgb, 1))

run(s.big_chase(5))
