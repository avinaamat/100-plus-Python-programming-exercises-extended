# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
#
my_list=[12,24,35,70,88,120,155]
sol=[k for k in my_list if k!=24]
#another option:
my_list.remove(24)
print(sol)
print(my_list)