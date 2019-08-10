from .Point import *
import matplotlib.pyplot as plt
import numpy as np

class DescendantGradient(object):

    # Returns te global minimum of the function
    @staticmethod
    def find_min(initial_value, func, learn_rate, precision, maximum=10000):

        # Initializes variables
        value = initial_value
        derivative = func.derive(value)

        # Defines maximum iteration quantity
        iteration = 0
        # Register all points visited during iterations
        values_visited = []

        # Iterate until the derivative value or maximum iteration has been reached
        while round(derivative.y, precision) != 0 and iteration < maximum:

            # Register visited value
            values_visited.append(Point(x=value, y=func.f(value).y))

            # Gets next x value and its derivative
            value = value - learn_rate * derivative.y
            derivative = func.derive(value)

            iteration += 1

        # return visited values and minimum x value
        return values_visited, Point(x=value, y=func.f(value).y), iteration

    @staticmethod
    def plot_analysis(title, func, visited_values, result, iterations, precision):
        title += ' - ' + str(iterations) + ' interations for ' + str(precision) + ' decimal points precision'

        # Configures ploting style and layout
        plt.style.use('seaborn-whitegrid')
        plt.title(title)
        plt.xlabel('x')
        plt.ylabel('y')

        # Gets analysed boundaries
        min_x = min([value.x for value in visited_values])
        max_x = max([value.x for value in visited_values])

        # Gets points to plot curve
        points = [func.f(i) for i in np.arange(min_x, max_x, 0.001)]

        # Plots curve in boundaries
        plt.plot([p.x for p in points], [p.y for p in points], color='#395C6B')

        # Plots visited points
        plt.plot([v.x for v in visited_values], [v.y for v in visited_values], 'ro', color='#C97064')

        # Plots result (final point)
        plt.plot([result.x], [result.y], 'ro', color='#32965D')

        # Shows the legend and result value
        plt.legend(['f(x)', 'Visited Values', 'Result (x = ' + str(result.x) + '; y = ' + str(result.y) + ')'],
                   loc='upper left')

        plt.show()

