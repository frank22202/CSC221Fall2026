with open('scores.txt', 'a') as file:
    score = input('Enter score: ')
    #file.write(score)
    while 0 <= int(score) <= 100:
        file.write(score + '\n')
        score = input('Enter score(-1 to exit): ')