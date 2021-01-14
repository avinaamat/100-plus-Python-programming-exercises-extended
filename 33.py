# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
#
l=lambda start,end: [i*i for i in range(start,end+1)]
print(l(1,20))