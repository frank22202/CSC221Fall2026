names = ['Smith'] * 3
print(type(names))

names.append('White')
names.append('Adams')
names.extend(['Bill', 'John', 'Michelle'])
names.insert(3, 'Ethan')
names.insert(0, 'David')
names.remove('Smith')
names.pop(3)
names.pop()
print(names)
