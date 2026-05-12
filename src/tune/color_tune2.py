from random import shuffle
from asyncio import sleep, create_task, run
from control.lumen import Lumen

lumen = Lumen()


def start() -> None:
    lumen.strip.begin()
    lumen.all_off()


async def scene4(loop_cnt) -> None:
    colors = [c for c in lumen.COLORS if c.name in ("PINK", "PURPLE", "BLUE")]
    # colors = [c for c in lumen.COLORS if c.name in ("RED","GREEN","BLUE")]
    for _ in range(0, loop_cnt):
        shuffle(colors)
        print("Set Start")
        print(f"0: {colors[0].name}")
        print(f"1: {colors[1].name}")
        print(f"2: {colors[2].name}")
        await lumen.color_on("big", colors[0].rgb)
        await lumen.color_on("small_b", colors[1].rgb)
        await lumen.color_on("small_f", colors[2].rgb)
        await sleep(3)
        lumen.all_off()


if __name__ == "__main__":
    start()
    while True:
        run(scene4(1))  # shuffl led
