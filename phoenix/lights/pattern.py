from phoenix.coordinates.triangles import get_outer_edges

OUTER_EDGE_PATTERN = 0

class Pattern:
    def __init__(
        self,
        pattern = OUTER_EDGE_PATTERN,
        tail_length = 6
    ):
        self.pattern = pattern
        self.pattern_array = get_outer_edges()
        self.length = len(self.pattern_array)
        self.current = 0
        self.tail_length = tail_length

    def get_range(self):
        range = []
        for i in range(0, self.tail_length):
            address = self.pattern_array[(self.current-i) % self.length]
            range.append(address)

        self.current = (self.current+1) % self.length
        return range

    def get_next(self):
        next = self.pattern_array[self.current]
        self.current = (self.current+1) % self.length
        return next

    def get_tail(self):
        tail = (self.current-self.tail_length) % self.length
        return self.pattern_array[tail]
