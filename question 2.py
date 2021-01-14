# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320
# def fact(num):
#     count = 1
#     for i in range(1, num + 1):
#         count *= i
#     print(count, end=', ')
#
#
# while True:
#     x = input("enter a num: ")
#     if x == 'q':
#         break
#     fact(int(x))
# print('finished')

# preferred answer:
from functools import reduce

def red(acc, item):
    return acc * item

x = int(input())
print(reduce(red, range(1, x+1), 1))
