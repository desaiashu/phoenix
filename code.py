from phoenix.interface.display import Display
from phoenix.interface.knobs import Knobs
from phoenix.lights.lights import Lights
from phoenix.composition.composer import Composer


display = Display()
lights = Lights()

composer = Composer(lights, 10, 10, display)
knob_handlers = [composer.brightness_handler, composer.speed_handler, composer.brightness_handler]

knobs = Knobs(knob_handlers)

composer.knobs = knobs

print('yay')

count = 0

# Run loop
while True:
    composer.update()
    if count % composer.speed*5 == 0:
        knobs.update()
    count+=1

