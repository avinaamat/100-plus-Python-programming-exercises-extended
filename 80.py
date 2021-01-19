# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
#
my_list = [5, 6, 77, 45, 22, 12, 24]
red = list(filter(lambda i: i % 2, my_list))
print(red)

# could also use:
refined_list = [i for i in my_list if i % 2]
print(refined_list)
