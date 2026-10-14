# 1. variable 2. initial value 3. test 4. update
counter = total = 0

while counter < 5:
    score = int(input('Enter score: '))
    total += score
    counter += 1

print(f'the average score is {total/counter:.2f}')