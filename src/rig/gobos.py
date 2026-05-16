# fmt: off
from models.fixtures import Gobo, Frame, ColorSet

EYE = Gobo(
    name="eye",
    description="Winking eye gobo",
    frames=(
        Frame(
            name="CloseEye1",
            ordinal=1,
            color_sets=(
                ColorSet(
                    ordinal=1,
                    leds=(
48, 108, 156, 196, 228, 252, 268, 280, 288, 284, 274, 260, 240, 212, 176, 132, 78
                    ),
                ),
            ),
        ),
        Frame(
            name="OpenEye",
            ordinal=2,
            color_sets=(
                ColorSet(
                    ordinal=1,
                    leds=(
            115,  120,  125,
        52,   162,  166,  170,    74,
        111,  201,  204,  207,   129,
                    ),
                ),
                ColorSet(
                    ordinal=2,
                    leds=(
    109, 158, 199, 209, 174, 131,
48,                               78,
    155, 194, 225, 215, 178, 133,
228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244,
245, 246, 247, 248, 249, 250, 251,
                    )   
                ),        
                ColorSet(
                    ordinal=3,
                    leds=(
268, 269, 270, 271, 272 , 273, 274, 275, 276, 277, 278, 279,
                    )   
                ),                              
            ),
        ),
        Frame(
            name="CloseEye2",
            ordinal=3,
            color_sets=(
                ColorSet(
                    ordinal=1,
                    leds=(

    # 45°
    114, 161, 200, 231, 254, 281,

    # 225°
    138, 181, 216, 243, 262, 285,


    # Ring1 5-way
    48, 60, 72, 84, 96,

    # Ring3 5-way
    156, 164, 172, 180, 188,

                    )   
                ),
            ),
        ),
    ),
)
