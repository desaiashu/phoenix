# Define the DotDict class
class DotDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

# Define the color palette in RGB format as a DotDict
colors = DotDict({
    "warm_white": (255, 223, 186),
    "soft_blue": (173, 216, 230),
    "amber": (255, 191, 0),
    "cool_white": (224, 240, 255),
    "muted_green": (144, 176, 144),
    "light_grey": (211, 211, 211),
    "dusty_rose": (205, 92, 92),
    "soft_lavender": (230, 230, 250),
    "none": (0, 0, 0),
})