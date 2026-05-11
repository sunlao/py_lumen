from random import shuffle
from asyncio import sleep, create_task, run
from control.lumen import Lumen

lumen = Lumen()


def start() -> None:
    lumen.strip.begin()
    lumen.all_off()    

async def increment(loop_cnt) -> None:
    for _ in range(0, loop_cnt):
        await lumen.increment_zone()

if __name__ == "__main__":
    start()
    while True:
        run(increment(1)) # shuffl led 

