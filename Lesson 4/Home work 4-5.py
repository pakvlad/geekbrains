from functools import reduce
def my_func(a,b):
    return a * b
print(b for b in range(100, 1001) if b % 2 == 0)
print(reduce(my_func,[b for b in range(100,1001) if b % 2 == 0]))