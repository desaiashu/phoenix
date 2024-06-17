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
    composer.update()  # Update the pattern and set the light colors based on the current state

    # Update colors at specific intervals
    if count % (composer.speed * 50) == 0:  # Every 50 iterations multiplied by the speed factor
        new_colors = [(255, 255, 0), (0, 255, 255), (255, 0, 0)]  # Define new colors
        composer.update_pattern_colors(new_colors)  # Update pattern colors

    if count % (composer.speed * 5) == 0:  # Update knobs at specific intervals
        knobs.update()

    count += 1
