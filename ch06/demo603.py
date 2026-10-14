import random

dice1 = random.randint(1, 6)

# counter1 = counter2 = counter3 = counter4 = \
#     counter5 = counter6 = 0
counter = [0] * 7
if dice1 == 1:
    counter[1] += 1
elif dice1 == 2:
    counter[2] += 1
elif dice1 == 3:
    counter[3] += 1
elif dice1 == 4:
    counter[4] += 1
elif dice1 == 5:
    counter[5] += 1
else:
    counter[6] == 1

print(counter[1])
print(counter[2])
print(counter[3])
print(counter[4])
print(counter[5])
print(counter[6])