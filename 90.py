# Please write a program which count and print the numbers of each character in a string input by console.
#
# Example: If the following string is given as input to the program:
#
# abcdefgabc
# Then, the output of the program should be:
#
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

n=input('enter sentence: ')
my_dict={}
for i in n:
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i] = 1
for j,k in my_dict.items():
    print(f'{j},{k}')