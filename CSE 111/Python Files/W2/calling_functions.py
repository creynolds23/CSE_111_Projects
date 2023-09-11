"""
Author: Conner Reynolds
Purpose: Practice calling functions
Date: 9/19/2022
"""
import math

## Get input from user
number_items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

## Calculations
number_boxes = math.ceil(number_items / items_per_box)

print(f'\nFor {number_items} items, packing {items_per_box} items in each box, you will need {number_boxes} boxes.')

