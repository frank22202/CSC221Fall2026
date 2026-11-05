list1 = [[1,2,'e'], ['John', 5, 2.3, 'Mary'], [1,2]]
for row in range(len(list1)):
    for column in range(len(list1[row])):
        print(list1[row][column], end=', ')
    print()
