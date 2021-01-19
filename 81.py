# By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
my_list = [12, 24, 35, 70, 88, 120, 155]
sol = list(filter(lambda i: i % 35 == 0, my_list))
print(sol)

refined_list = [i for i in my_list if i % 35 == 0]
print(refined_list)
