from .triangle_patterns import triangle_patterns

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
        next = self.pattern_array[self.current]
        self.current = (self.current+1) % self.length
        return next

    def get_tail(self):
        tail = (self.current-self.tail_length) % self.length
        return self.pattern_array[tail]

## not needed?
    # def get_range(self):
    #     range = []
    #     for i in range(0, self.tail_length):
    #         address = self.pattern_array[(self.current-i) % self.length]
    #         range.append(address)
    #
    #     self.current = (self.current+1) % self.length
    #     return range
