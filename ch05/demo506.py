scores1 = (87, 98, 'A', 100, 67)
scores2 = (87, 98, 'A', 100, 67)
scores3 = (87, 98, 'A', 100, 67)
scores4 = ('asb',)
print(type(scores4))

print(scores1 == scores2 == scores3) #True
print(scores1 is scores2 is scores3) #True

print(scores1[2:5])

scores2 = list(scores2)
scores2[1] = 'B'
scores2 = tuple(scores2)
print(scores2)

