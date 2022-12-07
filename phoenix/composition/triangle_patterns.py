from phoenix.coordinates.triangles import get_addresses_from_edge
from phoenix.coordinates.conversions import reverse

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


def doc_james_1():
    pattern = []
    # big middle triangle circling
    pattern.extend(reverse(get_addresses_from_edge(1, 1)));
    pattern.extend(reverse(get_addresses_from_edge(1, 3)));
    pattern.extend(reverse(get_addresses_from_edge(1, 2)));
    return pattern

def doc_james_2():
    pattern = []
    # big middle triangle circling
    pattern.extend(reverse(get_addresses_from_edge(2, 3)));
    pattern.extend(reverse(get_addresses_from_edge(2, 2)));
    pattern.extend(reverse(get_addresses_from_edge(2, 1)));
    return pattern

def doc_james_3():
    pattern = []
    # big middle triangle circling
    pattern.extend(reverse(get_addresses_from_edge(3, 2)));
    pattern.extend(reverse(get_addresses_from_edge(3, 1)));
    pattern.extend(reverse(get_addresses_from_edge(3, 3)));
    return pattern

def doc_james_4():
    pattern = []
    # big middle triangle circling
    pattern.extend(get_addresses_from_edge(4, 1));
    pattern.extend(get_addresses_from_edge(4, 2));
    pattern.extend(get_addresses_from_edge(4, 3));
    return pattern

def doc_james_5():
    pattern = []
    # big middle triangle circling
    pattern.extend(reverse(get_addresses_from_edge(5, 3)));
    pattern.extend(reverse(get_addresses_from_edge(5, 1)));
    pattern.extend(reverse(get_addresses_from_edge(5, 2)));
    return pattern

def doc_james_6():
    pattern = []
    # big middle triangle circling
    pattern.extend(reverse(get_addresses_from_edge(6, 1)));
    pattern.extend(reverse(get_addresses_from_edge(6, 3)));
    pattern.extend(reverse(get_addresses_from_edge(6, 2)));
    return pattern

def doc_james_7():
    pattern = []
    # big middle triangle circling
    pattern.extend(reverse(get_addresses_from_edge(7, 2)));
    pattern.extend(reverse(get_addresses_from_edge(7, 1)));
    pattern.extend(reverse(get_addresses_from_edge(7, 3)));
    return pattern

def doc_james_8():
    pattern = []
    # big middle triangle circling
    pattern.extend(get_addresses_from_edge(8, 3));
    pattern.extend(get_addresses_from_edge(8, 1));
    pattern.extend(get_addresses_from_edge(8, 2));
    return pattern


    # other 3 big triangles travel in line along the edges

    #little opposites of big triangles

triangle_patterns = {
    'outer_edge': outer_edge(),
    'outer_counter_clockwise': outer_counter_clockwise(),
    'inner_clockwise': inner_clockwise(),
    'doc_james_1': doc_james_1(),
    'doc_james_2': doc_james_2(),
    'doc_james_3': doc_james_3(),
    'doc_james_4': doc_james_4(),
    'doc_james_5': doc_james_5(),
    'doc_james_6': doc_james_6(),
    'doc_james_7': doc_james_7(),
    'doc_james_8': doc_james_8(),

}
