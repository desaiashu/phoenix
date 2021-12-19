from phoenix.coordinates.triangles import get_strip_index_from_address
from phoenix.composition.pattern import Pattern, TRIANGLE, GRID
from phoenix.composition.colors import color_patterns, merge_colors
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
                         Pattern(TRIANGLE, 'cross_pattern_1', 12, color_patterns['psychedelic'], [(0, 0, 0)], [
                             Pattern(TRIANGLE, 'cross_pattern_2', 12, color_patterns['psychedelic'], [(0, 0, 0)]),
                             Pattern(TRIANGLE, 'cross_pattern_3', 12, color_patterns['psychedelic'], [(0, 0, 0)]),
                             Pattern(TRIANGLE, 'cross_pattern_4', 12, color_patterns['psychedelic'], [(0, 0, 0)]),
                             Pattern(TRIANGLE, 'cross_pattern_5', 12, color_patterns['psychedelic'], [(0, 0, 0)]),
                             Pattern(TRIANGLE, 'cross_pattern_6', 12, color_patterns['psychedelic'], [(0, 0, 0)])
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
        changes = {}
        for pattern in self.patterns:
            for next_address, next_color in pattern.get_next():
                # Another pattern already wanted to modify this address
                # We have a conflict. Let's resolve:
                if next_address in changes:
                    changes[next_address] = merge_colors(changes[next_address], next_color)
                else:
                    changes[next_address] = next_color
                
                self.set_color(next_address, changes[next_address])

            for tail_address, tail_color in pattern.get_tail():
                # As long as some other pattern hasn't decided to write on our pixel then clean up:
                if tail_address not in changes:
                    self.set_color(tail_address, tail_color)

    def set_color(self, address, color):
        strip_index = get_strip_index_from_address(address)
        self.strips[strip_index['strip']].set_color(strip_index['index'], color)
