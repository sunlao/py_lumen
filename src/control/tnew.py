from asyncio import run
from time import sleep
from control.steps import Steps

s = Steps()

run(s.all_offshuffle_by_cologroup())
sleep(3)
run(s.all_off())
