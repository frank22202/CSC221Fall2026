import random

print(random.randint(1, 5))
print(random.randrange(1, 5))

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(dice1 + dice2)

print(random.choice(['yes', 'no', 'not sure']))