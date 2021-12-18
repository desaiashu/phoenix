import board
import neopixel

LEDS_PER_STRIP = 72
addresses = [board.D10, board.D11, board.D13]

class Strip:
    def __init__(
        self,
        num,
    ):
        self.pixel = neopixel.NeoPixel(addresses[num-1], LEDS_PER_STRIP)

    def set_color(self, index, color):
        self.pixel[index] = color

def get_address_from_strip_index(strip, index):
    return strip*LEDS_PER_STRIP+index

def get_strip_index_from_address(address):
    index = address % LEDS_PER_STRIP
    strip = (address - index) / LEDS_PER_STRIP
    address = {
        'strip': int(strip),
        'index': index
    }
    return address
