from time import sleep
from .pattern import Pattern, TRIANGLE, GRID
from .automata import AutomataGrid
from .colors import colors

MIN_SPEED = 1
MAX_SPEED = 10
MIN_BRIGHTNESS = 1
MAX_BRIGHTNESS = 10

class Composer:
    def __init__(
        self,
        lights,
        speed,
        brightness,
        audio,
        midi,
        display
    ):
        # self.patterns = [
                        #  Pattern(TRIANGLE, 'outer_counter_clockwise', 12, (255, 147, 44), (0, 0, 0)),
                        #  Pattern(TRIANGLE, 'inner_clockwise', 12, (255, 00, 255), (0, 0, 0)),
                        #  Pattern(TRIANGLE, 'inner_clockwise', 12, (255, 147, 44), (0, 0, 0)),
                        #  ]
        # self.patterns = [   ///// Purple & pink!
        #                  Pattern(TRIANGLE, 'outer_counter_clockwise', 12, (250, 40, 40), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'inner_clockwise', 12, (70, 0, 200), (0, 0, 0)),
        #                  ]
        self.patterns = [
                         Pattern(TRIANGLE, 'doc_james_1', 6, colors.amber, (0, 0, 0)),
                         Pattern(TRIANGLE, 'doc_james_2', 6, colors.amber, (0, 0, 0)),
                         Pattern(TRIANGLE, 'doc_james_3', 6, colors.amber, (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_4', 6, (35, 76, 130), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_5', 3, (130, 30, 70), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_6', 3, (130, 30, 70), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_7', 3, (130, 30, 70), (0, 0, 0)),
        #                  Pattern(TRIANGLE, 'doc_james_8', 3, (130, 30, 70), (0, 0, 0)),
                         ]
        
        self.lights = lights
        self.audio = audio
        self.midi = midi
        self.speed = speed
        self.brightness = brightness
        self.display = display

        self.automata = AutomataGrid()
        self.x = 1
        self.update_display()

    def update(self):
        i = 1
        for pattern in self.patterns:
            if i < 5 or self.x % 2:
                next_pos = pattern.get_next()
                tail_pos = pattern.get_tail()
                self.lights.set_color(next_pos, pattern.color, self.brightness)
                self.lights.set_color(tail_pos, pattern.tail_color, self.brightness)
            self.x += 1
            i += 1
        sleep(0.1 / ((self.speed * 5) ** 2))

    def brightness_handler(self, delta):
        brightness = self.brightness + delta/2.0
        if brightness > MAX_BRIGHTNESS:
            brightness = MAX_BRIGHTNESS
        elif brightness < MIN_BRIGHTNESS:
            brightness = MIN_BRIGHTNESS
        self.brightness = brightness
        self.update_display()

    def speed_handler(self, delta):
        speed = self.speed + delta/2.0
        if speed > MAX_SPEED:
            speed = MAX_SPEED
        elif speed < MIN_SPEED:
            speed = MIN_SPEED
        self.speed = speed
        self.update_display()

    def update_display(self):
        self.display.update(self.speed, self.brightness)

    def update_pattern_colors(self, new_colors):
        for pattern, new_color in zip(self.patterns, new_colors):
            pattern.update_color(new_color)
