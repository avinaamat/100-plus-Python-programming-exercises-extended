# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
#
# Different sizes of alphabet rangoli are shown below:
#
# #size 3
#
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
#
# #size 5
#
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
from string import ascii_lowercase

n = int(input('enter number for rangoli: '))
sign=str(input('enter sign: '))
lower = ascii_lowercase[:n]
print(lower)
for row in range(-n + 1, n):
    abs_row = abs(row)
    dash_count = sign * abs_row * 2
    print(dash_count + sign.join(lower[:abs_row:-1] + lower[abs_row:n:]) + dash_count)
