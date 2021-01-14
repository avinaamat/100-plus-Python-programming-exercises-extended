# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
#
s=lambda start,end: print({i:i*i for i in range(start,end+1)})
s(1,20)