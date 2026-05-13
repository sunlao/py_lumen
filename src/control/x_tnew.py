from asyncio import run
from time import sleep
from control.steps import Steps

s = Steps()

run(s.all_shuffle_by_color_group())
# sleep(1)
run(s.all_off())
