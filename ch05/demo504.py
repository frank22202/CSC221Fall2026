import sys

scores = [89, 97.5, 'A', 'Pass', [78, 90, 'Fail']]
print(sys.getsizeof(scores))
scores = scores + scores
print(sys.getsizeof(scores))
scores.append(scores)
print(sys.getsizeof(scores))