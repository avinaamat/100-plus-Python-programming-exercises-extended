# Write a program that accepts a sentence and calculate the number of letters and digits.
#
# Suppose the following input is supplied to the program:
#
# hello world! 123
# Then, the output should be:
#
# LETTERS 10
# DIGITS 3
x = input()
Letters_count = Digit_count = 0
for c in x:
    if 'a' < c < 'z' or 'A' < c < 'Z':
        Letters_count += 1
    elif '0' < c < '9':
        Digit_count += 1
print(f'LETTERS {Letters_count}\nDIGITS {Digit_count}')

# another sol:
import re

input_string = input('> ')
print()
counter = {"LETTERS": len(re.findall("[a-zA-Z]", input_string)), "NUMBERS": len(re.findall("[0-9]", input_string))}

print(counter)
