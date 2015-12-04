#!/usr/bin/env python
from inputs import day1 as instructions

floor = 0
reach_basement = False
basement = 0
max_floor = 0
min_floor = 0

for i in instructions:
    basement = basement + 1
    if i == "(":
        floor = floor + 1
        max_floor = max(floor, max_floor)
    else:
        floor = floor - 1
        min_floor = min(floor, min_floor)
        if not reach_basement and floor < 0:
            reach_basement = True
            print("Reached basement on step {}".format(basement))

print("Total floors traversed: {}".format(len(instructions)))
print("Final floor reached: {}".format(floor))
print("Lowest floor reached: {}".format(min_floor))
print("Higest floor reached: {}".format(max_floor))
