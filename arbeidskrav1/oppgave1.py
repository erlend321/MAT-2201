import numpy as np

def f(x):
    return x**5 + x - 1

def s(x):
    return np.sin(x) -6*x - 5

def ln(x):
    return np.log(x) + x**2 - 3

def ivt(funksjon, a, b):
    print("f(x):")
    x_verdi = np.arange(a, b)
    for x in x_verdi:
        print(f"f({x:.1f}) = {funksjon(x):.2f}")
    print("\n")

if __name__ == "__main__":
    ivt(f, 0, 2)
    ivt(s, -1, 1)
    ivt(ln, 1, 3)