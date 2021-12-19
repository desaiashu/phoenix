from rainbowio import colorwheel
from .strip import Strip, get_strip_index_from_address

class Lights:
    def __init__(
        self
    ):
        self.strips = [Strip(1), Strip(2), Strip(3)]
        self.clear_lights()

    def clear_lights(self):
        for l in self.strips:
            for i in range(0, 72):
                l.pixel[i] = (0, 0, 0)

    def set_color(self, address, color):
        strip_index = get_strip_index_from_address(address)
        self.strips[strip_index['strip']].set_color(strip_index['index'], color)
