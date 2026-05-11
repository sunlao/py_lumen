from random import shuffle
from asyncio import sleep, create_task, run
from control.lumen import Lumen

lumen = Lumen()


def start() -> None:
    lumen.strip.begin()
    lumen.all_off()    


async def scene4(loop_cnt) -> None:
    colors = [c for c in lumen.COLORS if c.name not in ("OFF", "WHITE")]
    for _ in range(0, loop_cnt):
        shuffle(colors)
        print("Set Start")
        print(f"0: {colors[0].name}")
        print(f"1: {colors[1].name}")
        print(f"2: {colors[2].name}")
        task_bg = create_task(lumen.shuffle_led("big", colors[0].rgb, 0.032))
        await sleep(0.75)
        task_b = create_task(lumen.shuffle_led("small_b", colors[1].rgb, 0.35))
        await sleep(0.75)
        task_f = create_task(lumen.shuffle_led("small_f", colors[2].rgb, 0.32))
        await task_bg
        await task_b
        await task_f
        lumen.all_off()

if __name__ == "__main__":
    start()
    while True:
        run(scene4(1)) # shuffl led 
