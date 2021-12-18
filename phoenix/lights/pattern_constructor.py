from phoenix.coordinates.triangles import get_addresses_from_edge

def reverse(pattern):
    return pattern[::-1]

def outer_edge():
    pattern = []
    pattern.extend(get_addresses_from_edge(1, 1))
    pattern.extend(get_addresses_from_edge(2, 1))
    pattern.extend(get_addresses_from_edge(2, 2))
    pattern.extend(get_addresses_from_edge(3, 2))
    pattern.extend(get_addresses_from_edge(3, 3))
    pattern.extend(get_addresses_from_edge(1, 3))
    return pattern

def outer_counter_clockwise():
    pattern = []
    pattern.extend(get_addresses_from_edge(1, 1))
    pattern.extend(get_addresses_from_edge(2, 1))
    pattern.extend(get_addresses_from_edge(2, 2))
    pattern.extend(get_addresses_from_edge(4, 2))
    pattern.extend(get_addresses_from_edge(4, 3))
    pattern.extend(get_addresses_from_edge(4, 1))
    pattern.extend(get_addresses_from_edge(3, 2))
    pattern.extend(get_addresses_from_edge(3, 3))
    pattern.extend(get_addresses_from_edge(1, 3))
    return pattern

def inner_clockwise():
    pattern = []
    pattern.extend(reverse(get_addresses_from_edge(5, 1)))
    pattern.extend(reverse(get_addresses_from_edge(5, 3)))
    pattern.extend(reverse(get_addresses_from_edge(5, 2)))
    pattern.extend(get_addresses_from_edge(8, 1))
    pattern.extend(reverse(get_addresses_from_edge(6, 2)))
    pattern.extend(reverse(get_addresses_from_edge(6, 1)))
    pattern.extend(reverse(get_addresses_from_edge(6, 3)))
    pattern.extend(get_addresses_from_edge(8, 2))
    pattern.extend(reverse(get_addresses_from_edge(7, 3)))
    pattern.extend(reverse(get_addresses_from_edge(7, 2)))
    pattern.extend(reverse(get_addresses_from_edge(7, 1)))
    pattern.extend(get_addresses_from_edge(8, 3))
    return pattern

patterns = {
    'outer_edge': outer_edge(),
    'outer_counter_clockwise': outer_counter_clockwise(),
    'inner_clockwise': inner_clockwise()
}
