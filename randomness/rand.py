#!/usr/bin/env python3.1

"""
Determine if the distribution of random numbers is even.

"""
import random
depth = int(input('max number is :'))
multiplier = int(input('duration multiplier is:'))
for l in range(0,20):
    sequence = []
    distribution = {}
    duration = depth * multiplier
    while duration:
        r = random.randint(1,depth)
        sequence.append(r)
        duration -= 1

    for i in range(1,depth+1):
        c = sequence.count(i)
        distribution[i]=c
    print(distribution.values())

    
                    
