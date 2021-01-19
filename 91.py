# Please write a program which accepts a string from console and print it in reverse order.
#
# Example: If the following string is given as input to the program:*
#
# rise to vote sir
# Then, the output of the program should be:
#
# ris etov ot esir
n=input('enter sentence: ')
print(n[::-1])
# another option:
print(''.join(reversed(n)))