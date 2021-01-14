# The Fibonacci Sequence is computed based on the following formula:
#
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
#
# Example: If the following n is given as input to the program:
#
# 7
# Then, the output of the program should be:
#
# 13
# In case of input data being supplied to the question, it should be assumed to be a console input.
n = int(input('enter number for fib: '))
# f = lambda x: f(x - 1) + f(x - 2) if x > 1 else x
li = [0,1]


if n < 1:
    print(n)
else:
    f2 = 0
    for i in range(2, n + 1):
        li.append(li[i - 1] + li[i - 2])
for i in li:
    print(str(i)+',', end='')
print('\b')
