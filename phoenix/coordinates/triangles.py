# Triangles is for outer and inner triangle based patterns

# Triangle order:
## Outer: Left, right, top, center
## Inner: Left, right, top, center

# Edge order:
## Base down: Bottom, right, top
## Base up: Right, top, left

from phoenix.lights.strip import get_strip_index_from_address, get_address_from_strip_index
from .conversions import triangle_to_strip

def get_address_from_edge(triangle, edge, index):
    strip_index = get_strip_index_from_edge(triangle, edge, index)
    return get_address_from_strip_index(strip_index['strip'], strip_index['index'])

def get_strip_index_from_edge(triangle, edge, index):
    tri = triangle_to_strip[triangle]
    strip = tri['strip']
    strip_index = tri['index'][(edge-1)*tri['edge_length']+index]
    return {'strip': strip, 'index': strip_index}

def get_addresses_from_edge(triangle, edge):
    addresses = []
    edge_length = triangle_to_strip[triangle]['edge_length']
    for i in range(0, edge_length):
        addresses.append(get_address_from_edge(triangle, edge, i))
    return addresses
