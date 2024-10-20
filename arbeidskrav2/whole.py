import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data
x_values = np.array([0.01, 0.02, 0.28, 0.33, 0.38, 0.56, 2.26, 2.35, 2.45, 
                     3.26, 3.65, 3.74, 5.43, 6.36, 7.24, 7.70, 8.02, 9.39])  # Gpc
y_values = np.array([0.01, 0.01, 0.19, 0.20, 0.27, 0.34, 1.26, 1.49, 1.46,
                     2.01, 2.23, 2.30, 2.82, 3.32, 3.52, 3.77, 3.80, 4.12])  # 10^5 km/s

# (a) Model 1: y(x) = ax + b (Linear fit)
def linear_model(x, a, b):
    return a * x + b

# Fit the data to the model
params_model_1, _ = curve_fit(linear_model, x_values, y_values)
a_1, b_1 = params_model_1
print(f"Model 1 (y = ax + b): a = {a_1:.4f}, b = {b_1:.4f}")

# Compute residual sum of squares for Model 1
residuals_model_1 = y_values - linear_model(x_values, a_1, b_1)
rss_model_1 = np.sum(residuals_model_1 ** 2)
print(f"Residual sum of squares (Model 1): {rss_model_1:.4f}")

# Hubble constant for Model 1
H_model_1 = a_1  # slope of the linear fit
print(f"Hubble constant from Model 1: H = {H_model_1:.4f} (10^5 km/s/Gpc)")


# (b) Model 2: y(x) = ax (Linear fit through origin)
def linear_origin_model(x, a):
    return a * x

# Fit the data to the model
params_model_2, _ = curve_fit(linear_origin_model, x_values, y_values)
a_2 = params_model_2[0]
print(f"Model 2 (y = ax): a = {a_2:.4f}")

# Compute residual sum of squares for Model 2
residuals_model_2 = y_values - linear_origin_model(x_values, a_2)
rss_model_2 = np.sum(residuals_model_2 ** 2)
print(f"Residual sum of squares (Model 2): {rss_model_2:.4f}")

# Hubble constant for Model 2
H_model_2 = a_2  # slope of the linear fit through origin
print(f"Hubble constant from Model 2: H = {H_model_2:.4f} (10^5 km/s/Gpc)")


# (c) Model 3: y(x) = ax^2 + bx
def quadratic_model(x, a, b):
    return a * x ** 2 + b * x

# Fit the data to the model
params_model_3, _ = curve_fit(quadratic_model, x_values, y_values)
a_3, b_3 = params_model_3
print(f"Model 3 (y = ax^2 + bx): a = {a_3:.4f}, b = {b_3:.4f}")

# Compute residual sum of squares for Model 3
residuals_model_3 = y_values - quadratic_model(x_values, a_3, b_3)
rss_model_3 = np.sum(residuals_model_3 ** 2)
print(f"Residual sum of squares (Model 3): {rss_model_3:.4f}")

# Hubble constant from Model 3
H_model_3 = b_3  # Hubble constant in our time is the coefficient of the linear term
print(f"Hubble constant from Model 3 (Hubble time): H = {H_model_3:.4f} (10^5 km/s/Gpc)")

# Hubble constant at 9000 Mpc (Model 3)
H_at_9000_Mpc = 2 * a_3 * 9.0 + b_3
print(f"Hubble constant at 9000 Mpc: H = {H_at_9000_Mpc:.4f} (10^5 km/s/Gpc)")


# (d) Model 4: y(x) = ax^3 + bx^2 + cx
def cubic_model(x, a, b, c):
    return a * x ** 3 + b * x ** 2 + c * x

# Fit the data to the model
params_model_4, _ = curve_fit(cubic_model, x_values, y_values)
a_4, b_4, c_4 = params_model_4
print(f"Model 4 (y = ax^3 + bx^2 + cx): a = {a_4:.4f}, b = {b_4:.4f}, c = {c_4:.4f}")

# Compute residual sum of squares for Model 4
residuals_model_4 = y_values - cubic_model(x_values, a_4, b_4, c_4)
rss_model_4 = np.sum(residuals_model_4 ** 2)
print(f"Residual sum of squares (Model 4): {rss_model_4:.4f}")

# Plotting all the models
x_plot = np.linspace(0, 10, 100)

plt.scatter(x_values, y_values, label="Data", color="black")

plt.plot(x_plot, linear_model(x_plot, a_1, b_1), label="Model 1: y = ax + b")
plt.plot(x_plot, linear_origin_model(x_plot, a_2), label="Model 2: y = ax")
plt.plot(x_plot, quadratic_model(x_plot, a_3, b_3), label="Model 3: y = ax^2 + bx")
plt.plot(x_plot, cubic_model(x_plot, a_4, b_4, c_4), label="Model 4: y = ax^3 + bx^2 + cx")

plt.xlabel("Distance (Gpc)")
plt.ylabel("Velocity (10^5 km/s)")
plt.legend()
plt.title("Curve Fitting to Hubble's Data")
plt.show()
