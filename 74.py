# Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
#
import random

ans = random.sample(range(35, 1001, 35), 5)
print(ans)