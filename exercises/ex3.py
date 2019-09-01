from NumericCalc.MonteCarlo import *
import time
import numpy as np


# Defines exercise toroid function
def toroide(values):
    first_term = values[2]**2 + (np.sqrt(values[0]**2 + values[1]**2) - 3.0)**2

    if first_term <= 1 and values[0] >= 1 and values[1] >= -3.0:
        return 1.0
    else:
        return 0.0


def ex3():

    # part 1
    #f = lambda x: 4.0 / (1 + x[0] ** 2)
    #mc = MonteCarlo(f)
    #result = mc.Integrate([0.0], [1.0], 1000000)
    #print(result)

    # part 2
    mc = MonteCarlo(toroide)
    start = time.time()
    result = mc.Integrate([1.0, -3.0, -1.0], [4.0, 4.0, 1.0], 1000000)
    end = time.time()

    # Prints result and execution time
    print("%.4f" % result)
    print(end - start)
