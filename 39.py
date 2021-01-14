# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
#
x=tuple(i for i in range(1,11))
even_x=tuple(i for i in x if not i%2)
print(x)
print(even_x)

# another sol:
tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(filter(lambda x : x%2==0,tpl))  # Lambda function returns True if found even element.
                                             # Filter removes data for which function returns False
print(tpl1)