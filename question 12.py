# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

my_list = list()
for i in range(1000, 3001):
    take = True
    for c in str(i):
        if (int(c) % 2 != 0):
            take = False
            break
    if take:
        my_list.append(str(i))
print(','.join(my_list))

# one line sol:
print(','.join([str(num) for num in range(1000, 3001) if all(map(lambda num: int(num) % 2 == 0, str(num)))]))
