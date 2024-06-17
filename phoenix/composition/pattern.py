from .triangle_patterns import triangle_patterns
import random


TRIANGLE = 0
GRID = 1

class Pattern:
    def __init__(
        self,
        type = TRIANGLE,
        pattern = 'outer_edge',
        tail_length = 6,
        color = (35, 76, 130),
        tail_color = (0, 0, 0)
    ):
        self.pattern = pattern
        if type == TRIANGLE:
            self.pattern_array = triangle_patterns[pattern]
        else:
            self.pattern_array = None
        self.length = len(self.pattern_array)
        self.current = 0
        self.tail_length = tail_length
        self.color = color
        self.tail_color = tail_color

    def get_next(self):
        next_pos = self.pattern_array[self.current]
        self.current = (self.current + 1) % self.length
        return next_pos

    def get_tail(self):
        tail_pos = (self.current - self.tail_length) % self.length
        return self.pattern_array[tail_pos]

    def should_be_lit(self, position):
        # Logic to determine if a position should be lit
        # Example: Only light up if within a certain range of the current position
        lit_range = 5  # Number of positions to light up
        return (position >= self.current and position < self.current + lit_range) or \
               (position + self.length >= self.current and position + self.length < self.current + lit_range)

    def generate_color_for_position(self, position):
        # Example logic: color gradient based on position
        r = int((position / self.length) * 255)
        g = int(((self.length - position) / self.length) * 255)
        b = 128  # Fixed value for simplicity
        return (r, g, b)

    def update_color(self, new_color):
        self.color = new_color
## not needed?
    # def get_range(self):
    #     range = []
    #     for i in range(0, self.tail_length):
    #         address = self.pattern_array[(self.current-i) % self.length]
    #         range.append(address)
    #
    #     self.current = (self.current+1) % self.length
    #     return range
