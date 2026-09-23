score = int(input("Enter score: "))
if 0 > score or score > 100:
    print('Invalid score')
    exit(1)
if score < 60:
    print('F')
elif score < 70:
    print('D')
elif score < 80:
    print('C')
elif score < 90:
    print('B')
else:
    print('A')