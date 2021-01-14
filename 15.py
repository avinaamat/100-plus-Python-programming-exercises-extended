# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#
# Suppose the following input is supplied to the program:
#
# 9
# Then, the output should be:
#
# 11106
x=input()
print(int(x)+int(2*x)+int(3*x)+int(4*x))

# using reduce and lambda:
# from functools import reduce
# x = input('please enter a digit:')
# reduce(lambda x, y: int(x) + int(y), [x*i for i in range(1,5)])