import numpy as np

class MonteCarlo(object):

    def __init__(self, function):
        self.f = function

    def Integrate(self, initial, final, n):

        # Gets n random points
        points = []
        # For each dimension
        for d in range(0, len(initial)):
            # Get a value between boundaries
            current_dimension = []
            for i in range(0, n):
                random_value = np.random.uniform(initial[d], final[d])
                current_dimension.append(random_value)
            points.append(current_dimension)

        # Calculates Volume
        volume = 1.0
        for d in range(0, len(initial)):
            volume = volume * (final[d] - initial[d])

        # Sums random points
        sum = 0.0
        for i in range(0, n):
            x_value = [points[d][i] for d in range(0, len(initial))]
            sum = sum + self.f(x_value)

        # Calculates result
        result = volume * sum / n

        return result

