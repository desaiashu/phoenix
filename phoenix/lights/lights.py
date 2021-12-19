from phoenix.coordinates.triangles import get_strip_index_from_address
from phoenix.composition.pattern import Pattern, TRIANGLE, GRID
from phoenix.composition.colors import color_patterns
from rainbowio import colorwheel
from .strip import Strip

class Lights:
    def __init__(
        self
    ):
        self.strips = [Strip(1), Strip(2), Strip(3)]
        self.patterns = [
                         Pattern(TRIANGLE, 'outer_counter_clockwise', 12, color_patterns['psychedelic'], [(0, 0, 0)]),
                         Pattern(TRIANGLE, 'flower_left', 12, color_patterns['psychedelic'], [(0, 0, 0)], [
                             Pattern(TRIANGLE, 'flower_right', 12, color_patterns['psychedelic'], [(0, 0, 0)])
                         ]),
                         Pattern(TRIANGLE, 'outer_counter_clockwise', 12, color_patterns['psychedelic'], [(0, 0, 0)], [
                             Pattern(TRIANGLE, 'inner_clockwise', 12, [(35, 76, 130)], [(0, 0, 0)]),
                         ]),
                         Pattern(TRIANGLE, 'outer_counter_clockwise', 12, [(35, 76, 130)], [(0, 0, 0)]),
                         Pattern(TRIANGLE, 'inner_clockwise', 12, [(130, 30, 70)], [(0, 0, 0)]),
                         ]
        self.clear_lights()

    def clear_lights(self):
        for l in self.strips:
            for i in range(0, 72):
                l.pixel[i] = (0, 0, 0)

    def handler(self):
        for pattern in self.patterns:
            # TODO: resolve conflicts
            for next_address, next_color in pattern.get_next():
                self.set_color(next_address, next_color)
            for tail_address, tail_color in pattern.get_tail():
                self.set_color(tail_address, tail_color)

    def set_color(self, address, color):
        strip_index = get_strip_index_from_address(address)
        self.strips[strip_index['strip']].set_color(strip_index['index'], color)
