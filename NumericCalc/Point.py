import math


class Point(object):

    # Initializes X and Y points
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Returns Euclidean Distance between point
    def calc_distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

