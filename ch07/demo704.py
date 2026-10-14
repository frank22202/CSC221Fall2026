import random

counter = 0
numbers = [0] * 13

while counter < 6_000_000:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    numbers[dice1 + dice2] += 1
    counter += 1

for i in range(2, 13):
    print(i, numbers[i])