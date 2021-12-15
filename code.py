import time
from time import sleep
import board
import busio

from phoenix.interface.display import Display
from phoenix.interface.buttons import Buttons


# Display initialization and callback
display = Display("", "")

def transport_step_callback(next_note):
    display.setLabel2(note_from_number(next_note))


# Button initialization and callback
def button_1_callback():
    display.setLabel1("")

buttons = Buttons(button_1_callback)


# Run loop
while True:
    buttons.checkClicks()
    time.sleep(0.005)
