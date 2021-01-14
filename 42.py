# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
#
x = [i for i in range(1, 11)]
s = filter(lambda i: not i % 2, map(lambda i: i ** 2, x))
print(list(s))
