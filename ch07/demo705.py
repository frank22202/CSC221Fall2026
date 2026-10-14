message = '''This is a test on Python
C++ is fast
Java is easy'''
total = 0
for ch in message:
    if ch == 'a':
        total += 1

print(total)

# names = ['Adam', 'John', 'Mary', 'David']
# for name in names:
#     print(name, 'Smith')

names = {'Adam', 'John', 'Mary', 'David', 'David', 'Michelle'}
for name in names:
    print(name)