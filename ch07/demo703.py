counter = total = 0

score = int(input('Enter score(-1 to exit): '))
while 0 <= score <= 100:
    total += score
    counter += 1
    score = int(input('Enter score(-1 to exit): '))

print(f'the average score is {total/counter:.2f}')