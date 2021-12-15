"""I2C rotary encoder NeoPixel color picker and brightness setting example."""
import board
from rainbowio import colorwheel
from adafruit_seesaw import seesaw, neopixel, rotaryio, digitalio

addresses = [0x37, 0x36, 0x3A]

class Knob:
    def __init__(
        self,
        num,
    ):
        self.seesaw = seesaw.Seesaw(board.I2C(), addresses[num-1])
        self.encoder = rotaryio.IncrementalEncoder(self.seesaw)
        self.seesaw.pin_mode(24, self.seesaw.INPUT_PULLUP)
        self.switch = digitalio.DigitalIO(self.seesaw, 24)
        self.pixel = neopixel.NeoPixel(self.seesaw, 6, 1)
        self.pixel.brightness = 0.5
        self.last_position = -1
        self.color = 0  # start at red
        self.num = num

    def handler(self):
        # negate the position to make clockwise rotation positive
        position = -self.encoder.position
        if position != self.last_position:

            if self.switch.value:
                # Change the LED color.
                if position > self.last_position:  # Advance forward through the colorwheel.
                    self.color += 1
                else:
                    self.color -= 1  # Advance backward through the colorwheel.
                self.color = (self.color + 256) % 256  # wrap around to 0-256
                self.pixel.fill(colorwheel(self.color))

            else:  # If the button is pressed...
                # ...change the brightness.
                if position > self.last_position:  # Increase the brightness.
                    self.pixel.brightness = min(1.0, self.pixel.brightness + 0.1)
                else:  # Decrease the brightness.
                    self.pixel.brightness = max(0, self.pixel.brightness - 0.1)

        self.last_position = position


class Knobs:
    def __init__(
        self,
    ):
        self.knobs = [Knob(1), Knob(2), Knob(3)]

    def handler(self):
        for k in self.knobs:
            k.handler()
