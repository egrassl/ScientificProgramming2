from .Point import *


class Function(object):

    # Initializes with lambda function for func and derivative
    def __init__(self, function, derivative=None, derivative_second=None, derivative_fourth=None):
        self.function = function
        self.derivative = derivative
        self.derivative_second = derivative_second
        self.derivative_fourth = derivative_fourth

    # Returns function value
    def f(self, x):
        return [Point(x=x, y=self.function(x)), self.function(x)]

    # Returns Derivative valueO
    def derive(self, x):
        return [Point(x=x, y=self.derivative(x)), self.derivative(x)]

    def derive2(self, x):
        return [Point(x=x, y=self.derivative_second(x)), self.derivative_second(x)]

    def derive4(self, x):
        return [Point(x=x, y=self.derivative_fourth(x)), self.derivative_fourth(x)]
