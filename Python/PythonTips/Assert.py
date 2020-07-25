#!/usr/bin/env python3

"""
The use of Assertion is to let developers find the likely root cause
of a bug more quickly. It should be never raised unless we have bug in your program
"""

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

# Now try applying this fucntion 
# Given the shoe price as 1500 rupees
shoes = {'name': 'Ambur Shoes', 'price': 1500}

# Now at 25% we should expect, 1125 Rupees
print(apply_discount(shoes,0.25))

# Now apply invalid discounts. like 200% it should throw AssertError
print(apply_discount(shoes,2.0))

# Two pitfalls of using Assert Statements

# 1) Never Use Assestion for Data Validatation
# 2) Asserts thats Never Fail
#     eg) assert(1 == 2, 'This should Fail')

