from asyncio import Lock
from models.fixtures import Fixture, Fixtures, Leds
from rig.zones import SINGLE, THREE
from rig.gobos import EYE


class Rack:
    SMB = Fixture(
        name="smb",
        description="Small Circle Back",
        leds=Leds(start=0, stop=24),
        lock=Lock(),
    )
    SMF = Fixture(
        name="smf",
        description="Small Circle Front",
        leds=Leds(start=24, stop=48),
        lock=Lock(),
    )

    BIG = Fixture(
        name="big",
        description="Big Circle",
        leds=Leds(start=48, stop=289, gobo=EYE, zones=(SINGLE, THREE)),
        lock=Lock(),
    )

    RINGS = Fixtures(
        name="CP", description="Coin Pusher Installation", fixtures=(BIG, SMF, SMB)
    )
