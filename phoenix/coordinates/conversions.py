STRIP_INDEX_OUTER_LEFT = 1
STRIP_INDEX_OUTER_RIGHT = 0
STRIP_INDEX_INNER = 2

LEDS_PER_OUTER_EDGE = 12
LEDS_PER_INNER_EDGE = 6

def reverse(pattern):
    return pattern[::-1]
    
triangle_to_strip = {
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

#converts grid edge number to triangle edge number
#triangle, edge, start index
grid_to_triangle_edge = {
    1: (1, 1, 0),
    2: (1, 1, 6),
    3: (2, 1, 0),
    4: (2, 1, 6),
    5: (3, 1, 0),
    6: (3, 1, 6),
    7: (5, 2, 0), #rev
    8: (8, 1, 0),
    9: (6, 2, 0), #rev
    10: (7, 2, 0), #rev

    11: (3, 3, 0),
    12: (3, 3, 6),
    13: (1, 3, 0),
    14: (1, 3, 6),
    15: (2, 3, 0),
    16: (2, 3, 6),
    17: (7, 1, 0), #rev
    18: (8, 3, 0),
    19: (5, 1, 0), #rev
    20: (6, 1, 0), #rev

    21: (2, 2, 0),
    22: (2, 2, 6),
    23: (3, 2, 0),
    24: (3, 2, 6),
    25: (4, 2, 0),
    26: (4, 2, 6),
    27: (6, 3, 0), #rev
    28: (8, 2, 0),
    29: (7, 3, 0), #rev
    30: (5, 3, 0), #rev
}

grid_to_secondary_edge = {
    5: (4, 2, 0), #rev
    6: (4, 2, 6), #rev

    15: (4, 1, 0), #rev
    16: (4, 1, 6), #rev

    25: (4, 3, 0), #rev
    26: (4, 3, 6), #rev
}

grid_to_parallel_edge = {
    1: (3, 3, 0), #rev
    2: (3, 3, 6), #rev
    3: (3, 2, 0), #rev
    4: (3, 2, 6), #rev
    5: (4, 2, 0), #rev
    6: (4, 2, 6), #rev

    11: (2, 2, 0), #rev
    12: (2, 2, 6), #rev
    13: (2, 1, 0), #rev
    14: (2, 1, 6), #rev
    15: (4, 1, 0), #rev
    16: (4, 1, 6), #rev

    21: (1, 1, 0), #rev
    22: (1, 1, 6), #rev
    23: (1, 3, 0), #rev
    24: (1, 3, 6), #rev
    25: (4, 3, 0), #rev
    26: (4, 3, 6), #rev
}
