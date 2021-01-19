# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
#
my_list=[12,24,35,70,88,120,155]
sol=[k for i,k in enumerate(my_list) if i not in range(4,6) and i!=0]
print(sol)