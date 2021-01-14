# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#
# Suppose the following input is supplied to the program:
#
# Hello world!
# Then, the output should be:
#
# UPPER CASE 1
# LOWER CASE 9

x=input()
up=low=0
for c in x:
    if c.islower():
        low+=1
    elif c.isupper():
        up+=1
print(f'UPPER CASE {up}\nLOWER CASE {low}')