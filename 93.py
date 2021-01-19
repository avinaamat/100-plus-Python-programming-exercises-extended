# Please write a program which prints all permutations of [1,2,3]
#
from itertools import permutations

def permut_gen(li):
    for i in permutations(li):
        yield i

my_list=[1,2,3]
for j in permut_gen(my_list):
    print(j)
