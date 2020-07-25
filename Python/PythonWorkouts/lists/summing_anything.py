#!/usr/bin/env python

def mysum(*items):
    if not items:
        return items
    
    output = items[0]
    for item in items[1:]:
        output += item
    return output

print(mysum(()))
print(mysum(['1','2','3'],['1','2','3']))