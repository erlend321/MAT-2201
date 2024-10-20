import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


"""
Oppgave 2
"""


#Gpc
x = np.array([0.01, 0.02, 0.28, 0.33, 0.38, 0.56, 2.26, 2.35, 2.45,
             3.26, 3.65, 3.74, 5.43, 6.36, 7.24, 7.70, 8.02, 9.39])
#10**5 km/s
y = np.array([0.01, 0.01, 0.19, 0.20, 0.27, 0.34, 1.26, 1.49,
             1.46, 2.01, 2.23, 2.30, 2.82, 3.32, 3.52, 3.77, 3.80, 4.12])


"""
2a
Linear fit
"""
# least square
A = np.vstack([x, np.ones(len(x))]).T

a, b = np.linalg.lstsq(A, y, rcond=None)[0]

#Beregner hubble konstanten
hubble_contant = a * 100 #konverterer til (km/s)/mpc

#sum av kvadrat rest
y_p = a * x + b

ssr = np.sum((y - y_p) **2)

"""
2b
Linear fit through origin
"""

def linear_origin_model(x, a):
    return a * x

model_2, _ = curve_fit(linear_origin_model, x, y)
a_model_2 = model_2[0]

residuals_model_2 = y - linear_origin_model(x, a_model_2)
ssr_2 = np.sum(residuals_model_2 ** 2)

hubble_2 = a_model_2 * 100

"""
2c
quadratic fit
"""

def quad(x, a, b):
    return a * x **2 + b * x

model_3, _ = curve_fit(quad, x, y)
a_model_3, b_model_3 = model_3

residuals_model_3 = y - quad(x, a_model_3, b_model_3)
ssr_3 = np.sum(residuals_model_3 ** 2)

hubble_3 = b_model_3 * 100

hubble_9000_mpc = (2 * a_model_3 * 9 + b_model_3) * 100


"""
2d
cubic fit
"""

def cube(x, a, b, c):
    return a * x ** 3 + b * x ** 2 + c * x

model_4, _ = curve_fit(cube, x, y)
a_model_4, b_model_4, c_model_4 = model_4

residuals_model_4 = y - cube(x, a_model_4, b_model_4, c_model_4)
ssr_4 = np.sum(residuals_model_4 ** 2)

hubble_4 = a_model_4 * 100




if __name__=="__main__":
    print(f"Model 1, linear fit:\n")
    print(f"A = \n{A}")
    print(f"The Hubble constant (Slope): {hubble_contant:.4f} km/s per Mpc")
    print(f"Fitted model: y = {a:.2f}x + {b:.2f}")
    print(f"The sum of squared res: {ssr:.3f}\n")

    print(f"Model 2, linear fit through origin\n")
    print(f"Hubble constant, model 2: {hubble_2:.2f} km/s per Mpc")
    print(f"Fitted model: y = {a_model_2:.2f} * x ")
    print(f"The sum of squared res: {ssr_2:.3f}\n")

    print(f"Model 3, square model\n")
    print(f"Hubble constant, model 3: {hubble_3:.2f} km/s per Mpc")
    print(f"Hubble constant at 9000 Mpc: {hubble_9000_mpc} km/s per Mpc")
    print(f"Fitted model: y = {a_model_3:.2f} * x^2 + {b_model_3} * x ")
    print(f"The sum of squared res: {ssr_3:.3f}\n")

    print(f"Model 4, cubic model\n")
    print(f"Fitted model: {a_model_4:.5f} *x^3 + {b_model_4:.2f} * x^2 + {c_model_4:.2f} * x")
    print(f"The sum of squared residuals: {ssr_4:.4f}")


    x_plot = np.linspace(0, 10, 100)

    plt.scatter(x, y, label="Data", color="black")

    plt.plot(x_plot, linear_origin_model(x_plot, a_model_2), label="Model 2: y = ax")
    plt.plot(x_plot, cube(x_plot, a_model_4, b_model_4, c_model_4), label="Model 4: y = ax^3 + bx^2 + cx")

    plt.xlabel("Distance (Gpc)")
    plt.ylabel("Velocity (10^5 km/s)")
    plt.legend()
    plt.title("Curve Fitting to Hubble's Data")
    plt.show()