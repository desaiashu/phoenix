# Grid is for edge-neighbor based or pixel-neighbor based animations

# x axis is along base of triangle
# y axis is along left edge
# z axis is along right edge, it can be derived from x and y
from .triangles import get_addresses_from_edge

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
        index = 1,
    ):
        self.axis = axis
        self.index = index
        self.pixels = self.calc_pixel_addresses()

    def calc_pixel_addresses():
        pixels = []

        return pixels

    def get_x_neighbor(self, dir=1):

        return self.edge_x_wrap(x, y)

    def get_y_neighbor(self, dir=1):

        return self.edge_y_wrap(x, y)

    def get_z_neighbor(self, dir=1):

        return self.edge_z_wrap(x, y)


class Grid:
    def __init__(
        self,
    ):
        self.edges = []
        for i in range(0, Z+1):
            axis_edges = []
            for j in range(0, 10):
                axis_edges.append[Edge(i, j)]
            self.edges.append(axis_edges)


class AutomataGrid(Grid):
    def __init__(
        self,
    ):
        self.super.__init__()

    def evolve():
        pass
