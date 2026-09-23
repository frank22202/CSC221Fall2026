names = ['John', 'Mary', 'Carl', 'Michelle', 'Mary', 'Mary',
         'David']
names1 = {'John', 'Mary', 'Ethan', 'Michelle', 'Mary', 'Mary',
         'Adam'}
names = set(names)
print(names)
print(names1)
print(names.difference(names1))
print(names.union(names1))
print(names.intersection(names1))
print(names.symmetric_difference(names1))
