scores = [89, 97.5, 'A', 'Pass', [78, 90, 'Fail']]
print(type(scores))
scores1 = [89, 97.5, 'A', 'Pass', [78, 90, 'Fail']]
print(scores == scores1) #True
print(scores is scores1) #False
print(id(scores))
print(id(scores1))
print(id(scores1) - id(scores))

print(scores[4][2])
print(scores[1:4])
print(scores[::2])
scores2 = scores[::]

scores.append(88)
scores.insert(3, 99)
scores.remove(97.5)
scores.pop(2)
print(scores)
