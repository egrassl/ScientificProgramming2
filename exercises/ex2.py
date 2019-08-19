from NumericCalc.Function import *
from NumericCalc.Integral import *
import numpy as np

def ex2():
    # Definitions for function 1
    f1_f = lambda x: np.power(np.e, x)
    f1_dev2 = f1_f
    f1_dev4 = f1_f
    f1 = Function(function=f1_f, derivative_second=f1_dev2, derivative_fourth=f1_dev4)

    # Definitions for function 2
    f2_f = lambda x: np.sqrt(1 - x**2)
    f2_dev2 = lambda x: (-1.0) * (1.0 / np.power(1.0 - x**2, 3.0/2.0))
    f2_dev4 = lambda x: (-1.0) * (12*x**2 + 3) / np.power(1 - x**2, 7.0/2.0)
    f2 = Function(function=f2_f, derivative_second=f2_dev2, derivative_fourth=f2_dev4)

    # Definitions for function 3
    f3_f = lambda x: np.power(np.e, -(x**2))
    f3_dev2 = lambda x: np.power(np.e, -x**2) * (4*x**2 - 2)
    f3_dev4 = lambda x: 4 * np.power(np.e, -x**2) * (4*x**4 - 12*x**2 + 3)
    f3 = Function(function=f3_f, derivative_second=f3_dev2, derivative_fourth=f3_dev4)

    # Defines error
    error = 0.00001

    # Executes for first function
    print("==========F1==========")
    Integral.integrate(f1, 0, 1, IntegralType.MEANPOINT, error)
    Integral.integrate(f1, 0, 1, IntegralType.TRAPEZOID, error)
    Integral.integrate(f1, 0, 1, IntegralType.SIMPSON, error)
    print()

    # Executes for second function
    print("==========F2==========")
    Integral.integrate(f2, 0, 1, IntegralType.MEANPOINT, error)
    Integral.integrate(f2, 0, 1, IntegralType.TRAPEZOID, error)
    Integral.integrate(f2, 0, 1, IntegralType.SIMPSON, error)
    print()

    # Executes for third function
    print("==========F3==========")
    Integral.integrate(f3, 0, 1, IntegralType.MEANPOINT, error)
    Integral.integrate(f3, 0, 1, IntegralType.TRAPEZOID, error)
    Integral.integrate(f3, 0, 1, IntegralType.SIMPSON, error)
    print()
    #print(str(r1))
