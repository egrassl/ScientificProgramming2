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
        return (b - a) * func((a + b)/2.0)

    # Trapezoid formula
    @staticmethod
    def trapezoid(func, a, b):
        return (b - a) * ((func(a) + func(b))/2.0)

    # Simpson formula
    @staticmethod
    def simpson(func, a, b):
        return (b - a) * ((func(a) + 4 * func((a + b)/2.0) + func(b))/6.0)

    # Mean point error
    @staticmethod
    def mean_point_error(func, step):
        derivative = Integral.derivative(func, step, 2)

        return (np.power(step, 3) / 24) * derivative

    # Trapezoid error
    @staticmethod
    def trapezoid_error(func, step):
        derivative = Integral.derivative(func, step, 2)

        return (-1) * (np.power(step, 3) / 12) * derivative

    # Simpson error
    @staticmethod
    def simpson_error(func, step):
        derivative = Integral.derivative(func, step, 4)

        return (-1) * (np.power(step, 5)/2880) * derivative

    # Returns the derivative of a function with a given order
    @staticmethod
    def derivative(func, x, order):
        delta_x = 0.00001

        if order == 1:
            return (func(x + delta_x) - func(x)) / delta_x
        else:
            return (Integral.derivative(func, x + delta_x, order - 1) - Integral.derivative(func, x, order - 1)) / delta_x

    # Return intervals to calculations
    @staticmethod
    def get_intervals(init, end, n_intervals):
        intervals = []

        # Gets step value
        step = (end - init) / n_intervals

        # Creates array with measuring intervals
        for i in range(n_intervals + 1):
            intervals.append(init + i * step)

        # returns measuring intervals and step
        return intervals, step

    @staticmethod
    def integrate(func, a, b, type, err, inte):

        # Defines what method will be used
        # For Mean Point
        if type == IntegralType.MEANPOINT:
            formula = Integral.mean_point
            error = Integral.mean_point_error

        # For Trapezoid
        elif type == IntegralType.TRAPEZOID:
            formula = Integral.trapezoid
            error = Integral.trapezoid_error

        # For Simpson
        else:
            formula = Integral.simpson
            error = Integral.simpson_error

        # Increases measuring points to reduce error until the desired value is reached
        sections = 1
        intervals, step = Integral.get_intervals(a, b, sections)

        while error(func, step) > err:
            sections = sections * 2
            intervals, step = Integral.get_intervals(a, b, sections)

        intervals, step = Integral.get_intervals(a, b, inte)

        # Sums formula result for each interval and returns it as the integral value
        sum = 0
        for i in range(0, len(intervals) - 1):
            sum += formula(func, intervals[i], intervals[i+1])

        return sum
