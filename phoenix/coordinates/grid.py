# Grid is for edge-neighbor based or pixel-neighbor based animations

# x axis is along base of triangle
# y axis is along left edge
# z axis is along right edge, it can be derived from x and y
from .triangles import get_addresses_from_edge
from .conversions import reverse, grid_to_triangle_edge, grid_to_secondary_edge, grid_to_parallel_edge

X = 0
Y = 1
Z = 2

class Pixel:
    def __init__(
        self,
        edge,
        address
    ):
        self.edge = edge
        self.address = address

class Edge:
    def __init__(
        self,
        axis = X,
        index = 0,
    ):
        self.axis = axis
        self.index = index
        self.pixels = self.calc_pixel_addresses()
        self.secondary_pixels = self.calc_secondary_addresses()
        print(self.axis)
        print(self.index)
        print(self.pixels)
        print(self.secondary_pixels)

    def calc_pixel_addresses(self):
        pixels = []
        (triangle, edge, index) = grid_to_triangle_edge[self.axis*10+self.index]
        addresses = get_addresses_from_edge(triangle, edge)
        if self.index < 6 and not 8:
            addresses = reverse(addresses)
        pixels = addresses[index:index+6]
        return pixels

    def calc_secondary_addresses(self):
        pixels = []
        if self.index == 5 or self.index == 6:
            (triangle, edge, index) = grid_to_secondary_edge[self.axis*10+self.index]
            addresses = get_addresses_from_edge(triangle, edge)
            pixels = reverse(addresses)[index:index+6]
        return pixels


class Grid:
    def __init__(
        self,
    ):
        self.edges = []
        for i in range(0, Z+1):
            axis_edges = []
            for j in range(1, 11):
                axis_edges.append(Edge(i, j))
            self.edges.append(axis_edges)
