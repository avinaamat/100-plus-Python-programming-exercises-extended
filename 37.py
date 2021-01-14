# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
#
s=lambda start,end: print(tuple(i**2 for i in range(start,end+1)))
s(1,20)