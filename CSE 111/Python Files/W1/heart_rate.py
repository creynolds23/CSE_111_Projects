"""
Date: 9/13/2022
Author: Conner Reynolds
Purpose: Inputs with arithmetic
"""

## Input from User
age = int(input('Please enter your age: '))

## Conversions and calculated for range of heart rate
max = 220 - age
low = (max * .65)
high = (max * .85)

## Display results to user
print(f'''When you exercise to strengthen your heart, you should
keep your heart rate between {low:.0f} and {high:.0f} beats per minute.''')