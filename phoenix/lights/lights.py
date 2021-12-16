import board
import neopixel

# class Pixels
addresses = [board.D10, board.D11, board.D13]

    # pixels[2][i] = (35, 76, 130)

class Light:
    def __init__(
        self,
        num,
    ):
        self.pixel = neopixel.NeoPixel(addresses[num-1], 72)

    def set_color(self, color):
        self.pixel.fill(color)

class Lights:
    def __init__(
        self,
    ):
        self.lights = [Light(1), Light(2), Light(3)]

    def set_color(self, num, color):
        self.lights[num].set_color(color)
