from .Point import *
import numpy as np
from enum import Enum


class IntegralType(Enum):
    MEANPOINT = 1
    TRAPEZOID = 2
    SIMPSON = 3


class Integral(object):

    # Mean Point Formula
    @staticmethod
    def mean_point(func, a, b):
        _, fx = func.f((a + b)/2.0)
        return (b - a) * fx

    # Trapezoid formula
    @staticmethod
    def trapezoid(func, a, b):
        _, fx_a = func.f(a)
        _, fx_b = func.f(b)
        return (b - a) * (fx_a + fx_b)/2.0

    # Simpson formula
    @staticmethod
    def simpson(func, a, b):
        _, fx_a = func.f(a)
        _, fx_b = func.f(b)
        _, fx_ab = func.f((a + b)/2.0)

        return (b - a) * (fx_a + 4 * fx_ab + fx_b)/6.0

    # returns the maximum derivative for a given function and an interval
    @staticmethod
    def get_max_derivative(deriv, a, b, step):
        values = []

        # Appends all the derivative values given a step
        x = a
        while x <= b:
            _, dx = deriv(x)
            values.append(dx)
            x += step

        # Gets and returns the maximum derivative value
        maximum = max(values)
        return maximum

    # Mean point error
    @staticmethod
    def mean_point_error(func, a, b, n):
        # Get maximum second derivative
        derivative = Integral.get_max_derivative(func.derive2, a, b, 0.0001)

        return np.abs((np.power(b - a, 3) / (24 * n**2)) * derivative)

    # Trapezoid error
    @staticmethod
    def trapezoid_error(func, a, b, n):
        # Get maximum second derivative
        derivative = Integral.get_max_derivative(func.derive2, a, b, 0.0001)

        return np.abs((-1) * (np.power(b - a, 3) / (12 * n**2)) * derivative)

    # Simpson error
    @staticmethod
    def simpson_error(func, a, b, n):
        # Get maximum fourth derivative
        derivative = Integral.get_max_derivative(func.derive4, a, b, 0.0001)

        return np.abs((-1) * (np.power(b - a, 5)/(2880 * n**4)) * derivative)


    # Return intervals to calculations
    @staticmethod
    def get_intervals(init, end, n_intervals):
        intervals = []

        # Gets step value
        step = (end - init) / n_intervals

        # Creates array with measuring intervals
        for i in range(n_intervals + 1):
            intervals.append(init + i * step)

        # Returns measuring intervals and step
        return intervals, step

    @staticmethod
    def integrate(func, a, b, type, err):

        # Defines what method will be used
        # For Mean Point
        if type == IntegralType.MEANPOINT:
            formula = Integral.mean_point
            error = Integral.mean_point_error
            name = "Mean Point"

        # For Trapezoid
        elif type == IntegralType.TRAPEZOID:
            formula = Integral.trapezoid
            error = Integral.trapezoid_error
            name = "Trapezoid"

        # For Simpson
        else:
            formula = Integral.simpson
            error = Integral.simpson_error
            name = "Simpson"

        # Increases measuring points to reduce error until the desired value is reached
        sections = 1
        intervals, step = Integral.get_intervals(a, b, sections)

        while error(func, a, b, len(intervals) - 1) > err:
            sections = sections * 2
            intervals, step = Integral.get_intervals(a, b, sections)

        # Sums formula result for each interval and returns it as the integral value
        sum = 0
        for i in range(0, len(intervals) - 1):
            sum += formula(func, intervals[i], intervals[i+1])

        # Prints result
        print(name + " ===> " + "result: " + "%.10f" % sum + " | subdivisions: " + str(sections) + " | error: " + "%.10f" % error(func, a, b, len(intervals) - 1))

        return sum
