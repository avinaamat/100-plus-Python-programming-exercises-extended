# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
#
# Suppose the following input is supplied to the program:
#
# 7
# Then, the output should be:
#
# 0
# 7
# 14

from time import time


def dividable(n):
    for i in range(0, n + 1):
        if not i % 7:
            yield i


n = int(input('enter num: '))
t1 = time()
for i in dividable(n):
    print(i)
t2 = time()

t3 = time()
for i in range(0, n + 1):
    if not i % 7:
        print(i)
t4 = time()
print(f'took {t2 - t1}')
print(f'took {t4 - t3}')
