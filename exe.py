from asyncio import run
from control.scene import Scene


async def execute():
    await Scene().execute()

if __name__ == "__main__":
    print("start")
    run(execute())
    print("end")