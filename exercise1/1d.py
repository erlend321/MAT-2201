import numpy as np

def largest_float():
    tall = 0.3
    while not (tall * 2 == float('inf')):
        tall *= 2
    
    while not (tall + (tall*0.3) == float('inf')):
        tall += tall / 2

    return tall

veldig_stort_tall = largest_float()
print(float(veldig_stort_tall))

