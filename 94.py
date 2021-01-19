# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the
# chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
#

def puzzle_solve(head_count, leg_count):
    # sol=False
    sol_list = []
    for chicken_head in range(head_count):
        rabit_head = head_count - chicken_head
        if chicken_head * 2 + rabit_head * 4 == leg_count:
            # sol=True
            sol_list.append((chicken_head, rabit_head))
    # if sol:
    return sol_list
    # else:
    #     return []


head_count = 35
leg_count = 94
print(puzzle_solve(head_count, leg_count))

# another solution:
import itertools

def animal_counter(lst):
    chickens = 0
    rabbits = 0
    for i in lst:
        if i == 2:
            chickens += 1
        elif i == 4:
            rabbits += 1
    print(f"Number of chickens is {chickens}\nNumber of rabbits is {rabbits}")


def animal_calculator(total_legs, total_heads, legs_of_each_species):
    combinations = itertools.combinations_with_replacement(legs_of_each_species, total_heads)
    correct_combos = []
    for i in list(combinations):
        if sum(i) == total_legs:
            correct_combos.append(i)
    print(correct_combos)
    for i in correct_combos:
        animal_counter(i)

animal_calculator(94, 35, legs_of_each_species=[2,4])