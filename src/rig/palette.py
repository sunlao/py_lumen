from models.colors import Colors, RGB, ColorGroup, FrameColorSets, FrameColorSet, ColorMap

class Palette:

    OFF = Colors(name="OFF", ordinal=0, rgb=RGB(red=0, green=0, blue=0))
    WHITE = Colors(name="WHITE", ordinal=1, rgb=RGB(red=255, green=255, blue=255))
    PURPLE = Colors(name="PURPLE", ordinal=2, rgb=RGB(red=100, green=0, blue=175))
    RED = Colors(name="RED", ordinal=3, rgb=RGB(red=255, green=0, blue=0))
    CYAN = Colors(name="CYAN", ordinal=4, rgb=RGB(red=0, green=180, blue=220))
    GREEN = Colors(name="GREEN", ordinal=5, rgb=RGB(red=20, green=120, blue=20))
    YELLOW = Colors(name="YELLOW", ordinal=6, rgb=RGB(red=255, green=180, blue=0))
    ORANGE = Colors(name="ORANGE", ordinal=7, rgb=RGB(red=255, green=50, blue=0))
    PINK = Colors(name="PINK", ordinal=8, rgb=RGB(red=254, green=0, blue=150))
    BLUE = Colors(name="BLUE", ordinal=9, rgb=RGB(red=0, green=0, blue=255))
    COLORS = ColorGroup(
        collection=(PURPLE, RED, CYAN, GREEN, YELLOW, ORANGE, PINK, BLUE)
    )

    EYE_FRAME_COLOR_SET = FrameColorSets(
        frame_color_sets=(
            FrameColorSet(
                name="CloseEye1",
                color_maps=(ColorMap(ordinal=1, rgb=PINK.rgb),),
            ),
            FrameColorSet(
                name="OpenEye",
                color_maps=(
                    ColorMap(ordinal=1, rgb=PURPLE.rgb),
                    ColorMap(ordinal=2, rgb=RED.rgb),
                    ColorMap(ordinal=3, rgb=BLUE.rgb),
                ),
            ),       
            FrameColorSet(
                name="CloseEye2",
                color_maps=(ColorMap(ordinal=1, rgb=GREEN.rgb),),
            ),
        ),                 
    )