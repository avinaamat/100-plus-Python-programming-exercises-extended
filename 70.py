# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
#
import random
from random import randint

x = randint(0, 10)
if x % 2 == 1:
    y = randint(0, 1)
    if y == 0:
        x += 1
    else:
        x -= 1
print(x)

# using list:
resp = [i for i in range(0, 11, 2)]
print(random.choice(resp))
