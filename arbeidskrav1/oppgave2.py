#bisection
import numpy as np

def g(x):
    return x**5 + x - 1

def s(x):
    return np.sin(x) - (6*x + 5)

def ln(x):
    if x <= 0:
        raise ValueError
    return np.log(x) + x**2 - 3


def bisection(f, a, b, tol = 1e-3):
    print(f"{'k':^10}{'a':^12}{'f(a)':^10}{'c':^12}{'f(c)':^10}{'b':^12}{'f(b)':^10}")
    k = 0

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        k += 1
        
        print(f"{k:^10}{a:^12.3f}{f(a)*(-1):^10.3f}{c:^12.3f}{f(c):^10.3f}{b:^12.3f}{-f(b):^10.3f}")
        
            
        if abs(f(c)) < tol:
            return c
        
        elif f(a) * f(c) < 0:
            b = c
        
        else:
            a = c
        
    return (a + b) / 2

if __name__ == "__main__":
    print("Finner rot for x^5 + x - 1")
    print(f"Rot til første funk: {bisection(g, -1, 2):.8f}\n\n")

    print("Finner rot for sin x - 6x + 5")
    print(f"Rot til andre funk: {bisection(s, -2, 3):.8f}\n\n")

    print("Finner rot for ln x + x^2 - 3")
    print(f"Rot til tredje funk: {bisection(ln, 1e-5, 3):.8f}\n")

        