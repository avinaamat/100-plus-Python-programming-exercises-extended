# You are given a date. Your task is to find what the day is on that date.
#
# Input
#
# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
#
# 08 05 2015
# Output
#
# Output the correct day in capital letters.
#
# WEDNESDAY

import calendar

n = input('enter date: ').split()
day = calendar.weekday(int(n[2]), int(n[0]), int(n[1]))
print(calendar.day_name[day].upper())
