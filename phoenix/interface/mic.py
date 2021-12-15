import time
import array
import math
import board
import audiobusio


# Remove DC bias before computing RMS.
def mean(values):
    return sum(values) / len(values)


def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )

    return math.sqrt(samples_sum / len(values))


# Main program
mic = audiobusio.PDMIn(board.TX, board.D12, sample_rate=16000, bit_depth=16)
samples = array.array('H', [0] * 160)


def mic_handler():
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    if magnitude > 7000:
        print((magnitude,))
