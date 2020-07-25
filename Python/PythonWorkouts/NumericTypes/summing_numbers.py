#!/usr/bin/env python

"""
Impelement a buit-in sum method
"""

def mysum(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

print(mysum(1,2,3,4,5,9,8))