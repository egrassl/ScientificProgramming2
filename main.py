from NumericCalc.Function import *
from NumericCalc.DescendantGradient import *


def main():
    # Problem constants
    x0 = 2
    precision = 4
    learn_rate = 0.1

    # Function a)
    f1_f = lambda x: x**2
    f1_dev = lambda x: 2*x
    f1 = Function(function=f1_f, derivative=f1_dev)

    # Function b)
    f2_f = lambda x: x**3 - 2*(x**2) + 2
    f2_dev = lambda x: 3*(x**2) - 4*x
    f2 = Function(function=f2_f, derivative=f2_dev)

    # Gets analysis results for Function a) and plots it
    points, result, iterations = DescendantGradient.find_min(initial_value=x0, func=f1, learn_rate=learn_rate,
                                                             precision=precision)
    DescendantGradient.plot_analysis("Func A", f1, points, result, iterations, precision)

    # Gets analysis results for Function b) and plots it
    points, result, iterations = DescendantGradient.find_min(initial_value=x0, func=f2, learn_rate=learn_rate,
                                                             precision=precision)
    DescendantGradient.plot_analysis("Func B", f2, points, result, iterations, precision)


main()
