from control.lumen import Lumen


async def test_start():
    await Lumen().start()
