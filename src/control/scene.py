from asyncio import sleep, create_task, run
from control.lumen import Lumen

lumen = Lumen()



def start() -> None:
    lumen.strip.begin()
    lumen.all_off()    


async def scene1(loop_cnt) -> None:
    for _ in range(0, loop_cnt):
        task_bg = create_task(lumen.shuffle_led_shuffle_color("big", 0.032))
        await sleep(0.5)
        task_b = create_task(lumen.shuffle_led_shuffle_color("small_b", 0.35))
        await sleep(0.5)
        task_f = create_task(lumen.shuffle_led_shuffle_color("small_f", 0.20))
        await task_bg
        await task_b
        await task_f
        lumen.all_off()

async def scene2(loop_cnt) -> None:
    task_b = create_task(lumen.flash_random("small_b", loop_cnt))
    task_f = create_task(lumen.flash_random("small_f", loop_cnt))
    task_bg = create_task(lumen.flash_random("big", loop_cnt))
    await task_b
    await task_f
    await task_bg
    lumen.all_off()

async def scene3(loop_cnt) -> None:
    for _ in range(0, loop_cnt):
        task_b = create_task(lumen.led_chase("small_b", 1, 0.125))
        task_f = create_task(lumen.led_chase("small_f", 1, 0.125))
        task_bg = create_task(lumen.big_led_chase(2, 0.05))
        await task_b
        await task_f
        await task_bg
        lumen.all_off()


if __name__ == "__main__":
    start()
    while True:
        run(scene1(1))
        run(scene2(1))
        run(scene3(1))
        run(scene2(1))
