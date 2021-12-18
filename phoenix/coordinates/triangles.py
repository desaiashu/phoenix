# Triangle order:
## Outer: Left, right, top, center
## STRIP_INDEX_INNER: Left, right, top, center

# Edge order:
## Base down: Bottom, right, top
## Base up: Right, top, left

STRIP_INDEX_OUTER_LEFT = 1
STRIP_INDEX_OUTER_RIGHT = 2
STRIP_INDEX_INNER = 0

LEDS_PER_OUTER_EDGE = 12
LEDS_PER_INNER_EDGE = 6
LEDS_PER_STRIP = 72

triangles = {
    1: {
        'strip': STRIP_INDEX_OUTER_LEFT,
        'index': [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12],
        'edge_length': LEDS_PER_OUTER_EDGE
    },
    2: {
        'strip': STRIP_INDEX_OUTER_RIGHT,
        'index': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
        'edge_length': LEDS_PER_OUTER_EDGE
    },
    3: {
        'strip': STRIP_INDEX_OUTER_LEFT,
        'index': [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71],
        'edge_length': LEDS_PER_OUTER_EDGE
    },
    4: {
        'strip': STRIP_INDEX_OUTER_RIGHT,
        'index': [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71],
        'edge_length': LEDS_PER_OUTER_EDGE
    },
    5: {
        'strip': STRIP_INDEX_INNER,
        'index': [5, 4, 3, 2, 1, 0, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        'edge_length': LEDS_PER_INNER_EDGE
    },
    6: {
        'strip': STRIP_INDEX_INNER,
        'index': [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 36, 37, 38, 39, 40, 41],
        'edge_length': LEDS_PER_INNER_EDGE
    },
    7: {
        'strip': STRIP_INDEX_INNER,
        'index': [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71],
        'edge_length': LEDS_PER_INNER_EDGE
    },
    8: {
        'strip': STRIP_INDEX_INNER,
        'index': [35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18],
        'edge_length': LEDS_PER_INNER_EDGE
    },
}

def get_address_from_edge(triangle, edge, index):
    strip_index = get_strip_index_from_edge(triangle, edge, index)
    return get_address_from_strip_index(strip_index['strip'], strip_index['index'])

def get_strip_index_from_edge(triangle, edge, index):
    tri = triangles[triangle]
    strip = tri['strip']
    strip_index = tri['index'][(edge-1)*tri['edge_length']+index]
    return {'strip': strip, 'index': strip_index}

def get_address_from_strip_index(strip, index):
    return strip*LEDS_PER_STRIP+index

def get_strip_index_from_address(address):
    index = address % LEDS_PER_STRIP
    strip = (address - index) / LEDS_PER_STRIP
    address = {
        'strip': int(strip),
        'index': index
    }
    return address

def get_addresses_from_edge(triangle, edge):
    addresses = []
    edge_length = triangles[triangle]['edge_length']
    for i in range(0, edge_length):
        addresses.append(get_address_from_edge(triangle, edge, i))
    return addresses
