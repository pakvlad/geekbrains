from itertools import count
from math import factorial

def symbol():
    for el in count(1):
        yield factorial(el)

gen = symbol()
x = 0
for i in gen:
    if x < 10:
        print(i)
        x += 1
    else:
        break