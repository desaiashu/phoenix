import time
from time import sleep
import board
import busio

from phoenix.interface.display import Display
from phoenix.interface.buttons import Buttons
from phoenix.interface.mic import mic_handler
from phoenix.interface.light_sensor import light_handler
from phoenix.interface.knobs import Knobs
from phoenix.lights.lights import Lights
import phoenix.interface.where_pdm


# Display initialization and callback
display = Display("", "")

def transport_step_callback(next_note):
    display.setLabel2(note_from_number(next_note))


# Button initialization and callback
def button_1_callback():
    display.setLabel1("")

buttons = Buttons(button_1_callback)

lights = Lights()
knobs = Knobs(lights.strips)

print('yay')

# Run loop
while True:
    # mic_handler()
    # light_handler()
    lights.handler()
    knobs.handler()
    buttons.checkClicks()
    # time.sleep(1)
    # time.sleep(0.005)
