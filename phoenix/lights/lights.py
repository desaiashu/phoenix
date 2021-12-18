import board
import neopixel

from phoenix.coordinates.triangles import get_strip_index_from_address
from .pattern import Pattern
from rainbowio import colorwheel

addresses = [board.D10, board.D11, board.D13]

class Strip:
    def __init__(
        self,
        num,
    ):
        self.pixel = neopixel.NeoPixel(addresses[num-1], 72)

    def set_color(self, index, color):
        self.pixel[index] = color

class Lights:
    def __init__(
        self
    ):
        self.strips = [Strip(1), Strip(2), Strip(3)]
        self.patterns = [
                         Pattern('outer_counter_clockwise', 12, (35, 76, 130), (0, 0, 0)),
                         Pattern('inner_clockwise', 12, (130, 30, 70), (0, 0, 0)),
                         ]
        self.clear_lights()

    def clear_lights(self):
        for l in self.strips:
            for i in range(0, 72):
                l.pixel[i] = (0, 0, 0)

    def handler(self):
        for pattern in self.patterns:
            self.set_color(pattern.get_next(), pattern.color)
            self.set_color(pattern.get_tail(), pattern.tail_color)

    def set_color(self, address, color):
        strip_index = get_strip_index_from_address(address)
        self.strips[strip_index['strip']].set_color(strip_index['index'], color)
