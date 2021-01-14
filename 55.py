# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
#
# Example: If the following words is given as input to the program:
#
# 22 cats and 34 dogs.
# Then, the output of the program should be:
#
# ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.

x = input().split()
print(list(filter(lambda i: '0' < i < '9', x)))
# using RE:
import re
y = input()
pattern = "(\d+)"
a=re.findall(pattern,y)
print(a)