
def regner_ut_epsilon():
    epsilon = 1
    while float(1 + epsilon) > 1:
        epsilon /= 2
    return epsilon * 2

flyttall = regner_ut_epsilon()
print(flyttall)





