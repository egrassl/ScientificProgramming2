from NumericCalc.Function import *
from NumericCalc.Integral import *
import numpy as np

def ex2():
    f1 = lambda x: np.power(np.e, x)
    f2 = lambda x: np.sqrt(1 - x**2)
    f3 = lambda x: np.power(np.e, -(x**2))

    r1 = Integral.integrate(f3, 0, 1, IntegralType.SIMPSON, 0.001, 1000)
    print(str(r1))
