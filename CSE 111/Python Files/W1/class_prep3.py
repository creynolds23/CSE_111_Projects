import math

def compute_area(r):
    return math.pi * r * r**2


radius = float(input("Please enter a radius: "))

print(f'The are is: {compute_area(radius)}')
