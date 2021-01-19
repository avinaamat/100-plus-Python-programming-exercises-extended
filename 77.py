# Please write a program to print the running time of execution of "1+1" for 100 times.
#
from time import time

t1 = time()
for i in range(100000):
    x = 1 + 1
print(f'it took {(time() - t1)} seconds long ')
