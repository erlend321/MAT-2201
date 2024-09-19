#FPI
import math
import numpy as np

def g(x):
    return (1 - x)**(1/5)

def s(x):
    return (math.sin(x) - 5) / 6

def ln(x):
    return (3 - np.log(x))**.5



def FPI(funk, xn, r):

    last_value = None
    values = []
    iterations = []
    iteration_count = 0
    tol = 1e-9


    print(f"{'x':^12}{'f(x)':^12}{'ei = |x - r|':^10}{'ei/ei-1':^12}")

    while True:
        xn = funk(xn)
        values.append(xn)

        iterations.append(iteration_count)
        iteration_count += 1
        
        
        error = abs(xn - r)

        if last_value is not None and error != 0:
            ratio = abs((last_value - r) / (xn - r))

        if last_value != None:
            print(f"{xn:^12.8f}{funk(xn):^12.8f}{error:^12.8f}{ratio:^12.8f}")
            
        if last_value != None:
            if abs(last_value - xn) < tol:
                print(f"\nIt converged at {xn:.8f}\n")
                break

        last_value = xn

if __name__ == "__main__":
    FPI(g, 0.8, 0.75488281)
    FPI(s, -0.8, -0.97094727)
    FPI(ln, 1, 1.59228985)




