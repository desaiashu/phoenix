import time
import board
import digitalio
import analogio

class Analyzer:
    def __init__(self, StrobePin=board.D4, RstPin=board.D5, AnalogPin=board.A0):
        self._StrobePin = digitalio.DigitalInOut(StrobePin)
        self._StrobePin.direction = digitalio.Direction.OUTPUT
        self._RSTPin = digitalio.DigitalInOut(RstPin)
        self._RSTPin.direction = digitalio.Direction.OUTPUT
        self._DCPin = analogio.AnalogIn(AnalogPin)
        self.Maxband = 7
        self.RstState = False
        self._TimepointSt = time.monotonic()
        self.RstModule()

    def RstModule(self):
        self._StrobePin.value = False
        self._RSTPin.value = True
        self._StrobePin.value = True
        self._StrobePin.value = False
        self._RSTPin.value = False
        time.sleep(0.000072)

    def ReadFreq(self):
        value = [0]*self.Maxband
        if not self.RstState:
            self._TimepointSt = time.monotonic()
            self.RstState = True
        else:
            _TimepointNow = time.monotonic()
            if _TimepointNow - self._TimepointSt > 3:
                self.RstModule()
                self.RstState = False

        for band in range(self.Maxband):
            time.sleep(0.00001)
            value[band] = self._DCPin.value
            time.sleep(0.00005)
            self._StrobePin.value = True
            time.sleep(0.000018)
            self._StrobePin.value = False
        return value
    
    