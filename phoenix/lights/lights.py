import board
import neopixel

from phoenix.coordinates.triangles import get_address_from_edge, get_strip_index_from_address, get_outer_edges
from .pattern import Pattern
from rainbowio import colorwheel

# class Pixels
addresses = [board.D10, board.D11, board.D13]

    # pixels[2][i] = (35, 76, 130)

class Light:
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
        self.lights = [Light(1), Light(2), Light(3)]

        self.pattern = Pattern()

        for l in self.lights:
            for i in range(0, 72):
                l.pixel[i] = (0, 0, 0)

        # for i in range(0, 3):
        #     address = get_address_from_edge(1, 1, i)
        #     self.set_color(address, (35, 76, 130))
        #     print(address)

        # for i in range(0, 6):
        #     address = get_address_from_edge(1, 2, i)
        #     print(address)
        #     self.lights[address['strip']].pixel[address['index']] = (55, 0, 100)



        # l = self.lights[2]
        # for i in range(0, 50):
        #     l.pixel[i] = (35, 76, 130)

    def handler(self):
        # for i in self.pattern.get_range():
        #     self.set_color(i, (35, 76, 130))
        self.set_color(self.pattern.get_next(), (35, 76, 130))
        self.set_color(self.pattern.get_tail(), (0, 0, 0))

    def set_color(self, address, color):
        strip_index = get_strip_index_from_address(address)
        self.lights[strip_index['strip']].set_color(strip_index['index'], color)
