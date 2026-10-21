import math

def func1() -> tuple:
    name = 'Adam'
    score = 100
    address = '123 main st'
    return name, score, address #packing

help(math.pow)
print(func1())
print(func1)
name, score, address = func1() #unpacking
print(name, score, address)

