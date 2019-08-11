from NumericCalc.Function import *
from NumericCalc.DescendantGradient import *
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Problem constants
    x0 = 2
    precision = 4
    learn_rate = 1.0

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
                                                             precision=precision, maximum=200)
    DescendantGradient.plot_analysis("Func A", f1, points, result, iterations, precision)

    # Gets analysis results for Function b) and plots it
    points, result, iterations = DescendantGradient.find_min(initial_value=x0, func=f2, learn_rate=learn_rate,
                                                             precision=precision, maximum=3)
    DescendantGradient.plot_analysis("Func B", f2, points, result, iterations, precision, 1.0, 10.0)


def plot_learn_rate_over_iteration(title, rates, iterations):
    # Configures ploting style and layout
    plt.style.use('seaborn-whitegrid')
    plt.title(title + ' - Learn Rate X Number of Iterations')
    plt.xlabel('Learn Rate')
    plt.ylabel('Number of Iterations')

    plt.plot(rates, iterations)

    plt.show()


def main2():
    # Problem constants
    x0 = 2
    precision = 4
    learn_rate = 0.1

    # Function a)
    f1_f = lambda x: x ** 2
    f1_dev = lambda x: 2 * x
    f1 = Function(function=f1_f, derivative=f1_dev)

    # Function b)
    f2_f = lambda x: x ** 3 - 2 * (x ** 2) + 2
    f2_dev = lambda x: 3 * (x ** 2) - 4 * x
    f2 = Function(function=f2_f, derivative=f2_dev)

    results = []
    rates = []
    for i in np.arange(learn_rate, 1.1, 0.1):
        # Gets analysis results for Function a) and plots it
        points, result, iterations = DescendantGradient.find_min(initial_value=x0, func=f1, learn_rate=i,
                                                                 precision=precision, maximum=200)
        results.append(iterations)
        rates.append(i)

    plot_learn_rate_over_iteration('Func A', rates, results)

    results = []
    rates = []
    for i in np.arange(learn_rate, 1.1, 0.1):
        # Gets analysis results for Function a) and plots it
        try:
            points, result, iterations = DescendantGradient.find_min(initial_value=x0, func=f2, learn_rate=i,
                                                                 precision=precision, maximum=200)
            results.append(iterations)
        except Exception:
            results.append(200)

        rates.append(i)

    plot_learn_rate_over_iteration('Func B', rates, results)


#main()
main2()

