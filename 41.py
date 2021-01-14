# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
#
x=[i for i in range(1,11)]
sq=list(map(lambda i: i**2 ,x))
print(sq)