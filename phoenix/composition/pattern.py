import math
from .triangle_patterns import triangle_patterns
from .colors import merge_colors

TRIANGLE = 0
GRID = 1

class Pattern:
    def __init__(
        self,
        type = TRIANGLE,
        pattern = 'outer_edge',
        tail_length = 6,
        colors = [(35, 76, 130)],
        tail_colors = [(0, 0, 0)],
        children = []
    ):
        self.pattern = pattern
        if type == TRIANGLE:
            self.pattern_array = triangle_patterns[pattern]
        else:
            self.pattern_array = None
        self.length = len(self.pattern_array)
        self.current = 0
        self.tail_length = tail_length
        self.colors = colors
        self.colors_length = len(colors)
        self.tail_colors = tail_colors
        self.tail_colors_length = len(tail_colors)
        self.children = children
        self.epochs_elapsed = 0

    def next_epoch(self):
        self.epochs_elapsed += 1

        if self.epochs_elapsed > self.length:
            self.epochs_elapsed = 0
        
        return self.epochs_elapsed

    def get_next_color(self, colors, colors_length):
        first_color = colors[math.floor((self.epochs_elapsed / self.length) * colors_length)]
        second_color = colors[math.ceil((self.epochs_elapsed / self.length) * colors_length)]
        
        return merge_colors(first_color, second_color)

    def get_next(self, inner_step = 1):
        next = self.pattern_array[self.current]
        self.current = (self.current+1) % self.length
        changes = [(next, self.get_next_color(self.colors, self.colors_length))]

        # Get next for children and append to changes
        if self.children is not None:
            for child_pattern in self.children:
                changes.extend(child_pattern.get_next())

        self.next_epoch()

        return changes

    def get_tail(self):
        tail = (self.current-self.tail_length) % self.length
        tails = [(self.pattern_array[tail], self.get_next_color(self.tail_colors, self.tail_colors_length))]

        # Get tail for children
        if self.children is not None:
            for child_pattern in self.children:
                tails.extend(child_pattern.get_tail())

        self.next_epoch()
        return tails

## not needed?
    # def get_range(self):
    #     range = []
    #     for i in range(0, self.tail_length):
    #         address = self.pattern_array[(self.current-i) % self.length]
    #         range.append(address)
    #
    #     self.current = (self.current+1) % self.length
    #     return range
