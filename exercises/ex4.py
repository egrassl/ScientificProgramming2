from NumericCalc.MonteCarlo import *
import time
import numpy as np


# Defines exercise toroid function
def toroid(values):
    first_term = values[2]**2 + (np.sqrt(values[0]**2 + values[1]**2) - 3.0)**2

    if first_term <= 1 <= values[0] and values[1] >= -3.0:
        return 1.0
    else:
        return 0.0


def ex4():

    # defines toroid properties
    initial = [1.0, -3.0, -1.0]
    final = [4.0, 4.0, 1.0]
    n = 1000000

    # Defines parallel processing info
    comm = MPI.COMM_WORLD
    n_processors = comm.Get_size()
    n_each = int(n / n_processors)

    # Intializes Monte Carlo foreach component
    mc = MonteCarlo(toroid)

    # Start counting
    start = time.time()

    # Executes Monte Carlo
    result = mc.Integrate(initial, final, n_each)
    result = np.array(result, np.float)
    print("Process %d/%d finished calculation with result: %f with %d random numbers" %
          (comm.Get_rank(), n_processors, result, n_each))

    # Communicates with root processor to reduce the Monte Carlo result
    final_result = np.array(0.0, np.float)
    comm.Reduce(result, final_result, op=MPI.SUM, root=0)

    # Prints the result in the main processor
    if comm.Get_rank() == 0:
        r = final_result / n_processors
        end = time.time()
        print("Result: %.4f \nTime: %.4f" % (r, end - start))

    # Finalizes MPI communication
    MPI.Finalize()
