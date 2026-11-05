scores = [85, 65, 95, 72]
new_scores = sorted(scores)
print(scores)
print(new_scores)

scores.sort()
print(scores)

scores.sort(reverse=True)
print(scores)

names = ['david', 'Smith', 'Smith', 'White', 'Adams', 'Bill', 'John']
print(sorted(names, key=len))
print(sorted(names, key=str.lower))