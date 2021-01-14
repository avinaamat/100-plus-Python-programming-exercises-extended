# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.
#
def binSearch(A, H, L, x):
    if H < L:
        return -1
    m =int( L + (H - L) / 2)
    if A[m] == x:
        return m
    elif A[m] < x:
        return binSearch(a, H, m + 1, x)
    else:
        return binSearch(a, m - 1, L, x)


a = list(range(0, 234, 3))
a.sort()
n = input('enter an item to search for: ')

print(binSearch(a, len(a), 0, int(n)))
