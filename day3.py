#!/usr/bin/env python
from inputs import day3 as instructions

robot_instruction = instructions[::2]
santa_instruction = instructions[1::2]

if robot_instruction == santa_instruction:
    print("You did it wrong dummy!")


def vistited_houses(instructions):
    visited = []
    origin = (0, 0)
    for i in instructions:
        if i == "^":
            origin = (origin[0]+1, origin[1])
            visited.append(origin)
        elif i == "v":
            origin = (origin[0]-1, origin[1])
            visited.append(origin)
        elif i == ">":
            origin = (origin[0], origin[1]+1)
            visited.append(origin)
        elif i == "<":
            origin = (origin[0], origin[1]-1)
            visited.append(origin)

    return visited

solo_visit = vistited_houses(instructions)
combo_vist = vistited_houses(robot_instruction) + vistited_houses(santa_instruction)

print("Santa visited {} unique houses".format(len(set(solo_visit))))
print("Together they visited {} unique houses".format(len(set(combo_vist))))
