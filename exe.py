from asyncio import run
from control.scene import Scene


async def exceute():
    await Scene().exceute()

if __name__ == "__main__":
    print("start")
    run(exceute())
    print("end")