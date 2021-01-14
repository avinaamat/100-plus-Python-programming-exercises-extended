# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# my_tuple = ()
# my_list = []
#
# x = input('enter seq: ')
# num = ''
# for c in x:
#     if c != ',':
#         num += c
#     else:
#         # my_tuple += num
#         my_list.append(num)
#         num=''
# my_tuple=tuple(my_list)
# print(my_tuple)
# print(my_list)

#better solution:
lst = input().split(',')
print(lst)
print(tuple(lst))