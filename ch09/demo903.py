name = 'Mary Anne Smith'

first = name.find(' ')
second = name.find(' ', first + 1)
print(name[first+1:second])
print(name.find('nn'))
