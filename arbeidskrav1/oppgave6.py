#sensitivity of root-finding
# using bisection for task 6b



def f(x, e = 1e-3):
    return (1 + e)*x**3 - 3*x**2 + x - 3


def bisection(f, a, b, tol = 1e-8):
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
    print("Finner rot for (1 + e)*x**3 - 3*x**2 + x - 3")
    print(f"Rot til f(x): {bisection(f, 2, 4):.8f}\n\n")