from asyncio import Lock
from models.fixtures import Fixture, Fixtures, Leds, Zone, Zones


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
        leds=Leds(
            start=48,
            stop=289,
            zones=(
                Zones(
                    name="Single",
                    description="Single Ring Zones ",
                    group=(
                        Zone(name="Ring1", ordinal=1, start=48, stop=108),
                        Zone(name="Ring2", ordinal=2, start=108, stop=156),
                        Zone(name="Ring3", ordinal=3, start=156, stop=196),
                        Zone(name="Ring4", ordinal=4, start=196, stop=228),
                        Zone(name="Ring5", ordinal=5, start=228, stop=252),
                        Zone(name="Ring6", ordinal=6, start=252, stop=268),
                        Zone(name="Ring7", ordinal=7, start=268, stop=280),
                        Zone(name="Ring8", ordinal=8, start=280, stop=288),
                        Zone(name="Ring9", ordinal=9, start=288, stop=289),
                    ),
                ),
                Zones(
                    name="Three",
                    description="Three Ring Zones ",
                    group=(
                        Zone(name="Ring1-3", ordinal=1, start=48, stop=196),
                        Zone(name="Ring4-6", ordinal=2, start=196, stop=268),
                        Zone(name="Ring7-9", ordinal=3, start=268, stop=289),
                    ),
                ),
            ),
        ),
        lock=Lock(),
    )
    RINGS = Fixtures(
        name="CP", description="Coin Pusher Installation", fixtures=(BIG, SMF, SMB)
    )
