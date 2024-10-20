from math import pi

x_vals = []
x = -10*pi

while -10*pi <= x < 10*pi:
    x += (20*pi/200)
    x_vals.append(x)

print(x_vals)
print(len(x_vals))