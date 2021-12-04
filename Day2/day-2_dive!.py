# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:25:10 2021

@author: Chyt
"""
with open( r"C:\\Users\Chyt\Documents\GitHub\advent-of-code-2021\Day2\input.txt") as f:
    lines = f.readlines()
    
def dive_1(input):
    depth = 0
    horz = 0
    
    for l in input:
        direction = l.split(" ")
        if direction[0] == "forward":
            horz = horz + int(direction[1])
        elif direction[0] == "down":
            depth = depth + int(direction[1])
        elif direction[0] == "up":
            depth = depth - int(direction[1])
    
    product = depth * horz
    print(product)

def dive_2(input):
    depth = 0
    horz = 0
    aim = 0
    
    for l in input:
        direction = l.split(" ")
        if direction[0] == "forward":
            horz = horz + int(direction[1])
            if aim > 0:
                depth = depth + (aim * int(direction[1]))
        elif direction[0] == "down":
            aim = aim + int(direction[1])
        elif direction[0] == "up":
            aim = aim - int(direction[1])
    
    product = depth * horz
    print(product)

dive_1(lines)
dive_2(lines)
    
    