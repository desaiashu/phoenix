from .pattern import Pattern, TRIANGLE, GRID
from .automata import AutomataGrid

class Composer:
    def __init__(
        self,
        lights
    ):
        self.patterns = [
                         Pattern(TRIANGLE, 'outer_counter_clockwise', 12, (250, 40, 40), (0, 0, 0)),
                         Pattern(TRIANGLE, 'inner_clockwise', 12, (70, 0, 200), (0, 0, 0)),
                         ]
        # self.patterns = [
        #                  Pattern(TRIANGLE, 'doc_james_1', 6, (35, 76, 130), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_2', 6, (35, 76, 130), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_3', 6, (35, 76, 130), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_4', 6, (35, 76, 130), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_5', 3, (130, 30, 70), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_6', 3, (130, 30, 70), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_7', 3, (130, 30, 70), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_8', 3, (130, 30, 70), (0, 0, 0)),
        #                  ]
        self.lights = lights

        self.automata = AutomataGrid()
        self.x = 1

    def handler(self):
        i = 1
        for pattern in self.patterns:
            if i < 5 or self.x % 2:
                self.lights.set_color(pattern.get_next(), pattern.color)
                self.lights.set_color(pattern.get_tail(), pattern.tail_color)
            self.x += 1
            i += 1
