score = int(input('Enter score: '))
score = score // 10 * 10

match score:
    case _ if not 0 <= score <= 100:
        print('Invalid score')
        exit(1)
    case _ if score < 60:
        print('F')
    case 60:
        print('D')
    case 70:
        print('C')
    case 80:
        print('B')
    case 90:
        print('A')
    case _:
        print('A+')
