# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.


def generator_func(start, end):
    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            yield i


gen = generator_func(2000, 3201)

for i in gen:
    print(i, end=',')
print("\b")
