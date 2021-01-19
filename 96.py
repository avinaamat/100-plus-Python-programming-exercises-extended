# You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
#
# If the following string is given as input to the program:
#
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Then, the output of the program should be:
#
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

s_w = input('enter string and width with space: ').split()
width = int(s_w[1])
for j in range(0, len(s_w[0]), width):
    print(s_w[0][j:j + width])

# another option:
import textwrap

print('\n'.join(textwrap.wrap(s_w[0], width=width)))
