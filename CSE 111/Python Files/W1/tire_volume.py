"""
Date: 9/14/2022
Author: Conner Reynolds
Purpose: Create a program to find the volum of a tire
"""
import math
from datetime import date
## Use datetime to get the current date
current_date_time = date.today()

## Input from the user
tire_width = int(input('Enter the width of the tire in mm (ex 250): '))
aspect_ratio = int(input('Enter the aspect ration of the tire (ex 50): '))
diameter_wheel = int(input('Enter the diameter of the wheel in inches (ex 25): '))

## Math conversions
volume = ((math.pi * tire_width**2 * aspect_ratio) * (tire_width * aspect_ratio + 2540 * diameter_wheel)) / 10000000000
cans_soda = (volume * 33.814) / 12
## Display results
print(f'\nThe approximate volume is {volume:.2f} liters')
print(f'The approximate amount of soda cans is {cans_soda:.1f} cans')

## Convert all intergers to string for txt file
tire_width = str(tire_width)
aspect_ratio = str(aspect_ratio)
current_date_time = str(current_date_time)
diameter_wheel = str(diameter_wheel)
volume = str(round(volume,2))

## Open the file to append
with open("volumes.txt", 'at') as volume_f:
    volume_f.write(f'{current_date_time}, {tire_width}, {aspect_ratio}, {diameter_wheel}, {volume}\n')
## Close the file
volume_f.close()

## If statement for user to purchase
purchase = str(input(print('Do you want to buy the tires(Enter yes or no)?  ')))

if purchase.lower() == 'yes':
    phone_number = str(input(print("Please input your phone number")))
    with open("volumes.txt", 'at') as volume_f:
        volume_f.write(f'{current_date_time}, {tire_width}, {aspect_ratio}, {diameter_wheel}, {volume}, {phone_number}\n')
## Close the file
    volume_f.close()
else:
    print("Thank you for coming in. Have a great day!")

