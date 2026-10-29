names = ('John', 'Mary', 'Adam', 'Amy', 'Michael')
delimiter = '@'
email = 'john@nvcc.edu'
data = email.split('@')
print(data)
print(delimiter.join(names))
print('John@Mary@Adam@Amy@Michael'.split(delimiter))
