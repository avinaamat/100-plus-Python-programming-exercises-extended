# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# The function should just print the keys only.
#

s = lambda start, end: print({i: i * i for i in range(start, end + 1)}.values())
# print(s(1, 20).values())
s(1, 20)