#!/usr/bin/env python
from inputs import day2 as box_input


def ribbon_for_box(l, w, h):
    side = 2 * (h + l)
    front = 2 * (h + w)
    top = 2 * (l + w)
    
    smallest = min(side, front, top)
    volume = l * h * w
    total = smallest + volume
    return total


def wrap_for_box(l, w, h):
    side = w * h
    front = l * h
    top = l * w

    smallest = min(side, front, top)
    total = 2*(side + front + top) + smallest
    return total

total_wrap = 0
total_ribbon = 0

for i in box_input:
    total_wrap = total_wrap + wrap_for_box(i[0], i[1], i[2])
    total_ribbon = total_ribbon + ribbon_for_box(i[0], i[1], i[2])

print("total wrap {}".format(total_wrap))
print("total ribbon {}".format(total_ribbon))