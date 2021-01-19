# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
#
my_3D_array=[[[0 for s in range(8)] for s in range(5)] for s in range(3)]
for x in my_3D_array:
    print(x)
