# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
#
my_list = [12, 24, 35, 70, 88, 120, 155]
sol = [k for i, k in enumerate(my_list) if i % 2]
print(sol)
