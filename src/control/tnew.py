from asyncio import run
from control.sequencer import Sequencer

s = Sequencer()

run(s.all_red_activate())
run(s.all_blue_random())
