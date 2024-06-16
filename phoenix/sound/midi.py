import board
import busio
import time
import adafruit_midi
from adafruit_midi.timing_clock import TimingClock

class Midi:
    def __init__(self):
        # Midi code below
        uart = busio.UART(board.TX, board.RX, baudrate=31250, timeout=0.001)  # init UART
        self.midi = adafruit_midi.MIDI(
            midi_in=uart,
            midi_out=uart,
            out_channel=0,
            debug=False,
        )
        self.BPM = 0
        self.last_time = time.time()
        self.alpha = 0.1 
        print("Midi output channel:", self.midi.out_channel + 1)

    def update(self):
        msg = self.midi.receive()

        if isinstance(msg, TimingClock):
            current_time = time.time()
            elapsed_time = current_time - self.last_time
            self.last_time = current_time

            # Calculate BPM
            bpm = 60 / (elapsed_time * 24)

            # Update self.BPM using exponential smoothing
            self.BPM = self.alpha * bpm + (1 - self.alpha) * self.BPM

            print("MIDI Clock message received, BPM:", self.BPM)
            
midi = Midi()
