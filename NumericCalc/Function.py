from .Point import *


class Function(object):

    # Initializes with lambda function for func and derivative
    def __init__(self, function, derivative):
        self.function = function
        self.derivative = derivative

    # Returns function value
    def f(self, x):
        return Point(x=x, y=self.function(x))

    # Returns Derivative value
    def derive(self, x):
        return Point(x=x, y=self.derivative(x))
