# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#
# Example:
#
# 0100,0011,1010,1001,100011001,0011,0101,01111
# Then the output should be:
#
# 1010
# Notes: Assume the data is input by console.

x = input().split(',')
s = ''
for i in x:
    if int(i, 2) % 5 == 0:
        s += i + ','
s += '\b'
print(s)

# one line solution:
print(*(binary for binary in input().split(',') if int(binary, base=2) % 5 == 0))

# lamdba:
data = input().split(',')
data = list(
    filter(lambda i: int(i, 2) % 5 == 0, data))  # lambda is an operator that helps to write function of one line
print(",".join(data))
