# f(n)=f(n-1)+100 when n>0
# and f(0)=0
# with a given n input by console (n>0).
#
# Example: If the following n is given as input to the program:
#
# 5
# Then, the output of the program should be:
#
# 500
# In case of input data being supplied to the question, it should be assumed to be a console input.

n = int(input('enter n: '))
prev = 0 + 100
for i in range(1, n):
    current = prev + 100
    prev = current
print(current)

# with lambda:
f = lambda n: f(n - 1) + 100 if n > 0 else 0
print(f(n))
