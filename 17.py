# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
#
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
#
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
#
# 500
D = W = 0
while True:
    x = input().split()
    if not x:
        break
    if x[0] == 'D':
        D += int(x[1])
    elif x[0] == 'W':
        W += int(x[1])
print(D - W)
