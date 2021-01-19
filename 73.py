# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
#
import random

ans = random.sample(range(100, 201, 2), 5)
print(ans)
