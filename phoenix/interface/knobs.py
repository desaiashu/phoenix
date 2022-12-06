"""I2C rotary encoder NeoPixel color picker and brightness setting example."""
import board
from adafruit_seesaw import seesaw, rotaryio, digitalio

addresses = [0x37, 0x36, 0x3A]

class Knob:
    def __init__(
        self,
        num,
        handler,
    ):
        self.seesaw = seesaw.Seesaw(board.I2C(), addresses[num-1])
        self.encoder = rotaryio.IncrementalEncoder(self.seesaw)
        self.seesaw.pin_mode(24, self.seesaw.INPUT_PULLUP)
        self.switch = digitalio.DigitalIO(self.seesaw, 24)

        self.last_position = -1
        self.num = num

        self.handler = handler

    def update(self):
        # negate the position to make clockwise rotation positive
        position = -self.encoder.position
        if position != self.last_position:
            self.handler(position - self.last_position)
            self.last_position = position
            

class Knobs:
    def __init__(
        self,
        handlers
    ):
        self.knobs = [Knob(1, handlers[0]), Knob(2, handlers[1]), Knob(3, handlers[2])]

    def update(self):
        for k in self.knobs:
            k.update()
