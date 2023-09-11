from audioop import reverse
import math
import random
from datetime import datetime
## Example 1 how many functions can call in 1 line of code
# print(int((abs(round(float(input("Enter a number: ")))))))

# ## Challenge #2 execute the print() function using 5 arguments
# print("Hello, I ", 20, sep=" am ", end =" how old are you?", flush=True)

## Challenge #3 Imort the math package and compute:
# def random_math():
#     return (math.ceil(math.pow(17, 9) / 3) - 6) % 2 ==0

# print(random_math())

## Challenge #4 import random package and make 
# rand_list= []
# while len(rand_list) < 100:
#     rand_list.append(random.randint(0, 1000))
# rand_list.sort(reverse=True)
# print(rand_list)

## Challenge #5 if it is an even minute (computer clock) print even minute or odd minute
now = datetime.now()
display_message = 'even minute'
if(now.minute % 2 > 0):
    display_message = 'odd minute'
print(display_message)