dict1 = {'DC':'District of Columbia',
         'MD':'Maryland',
         'VA':'Virginia',
         'CA':'California'}
print(dict1['CA'])
print(dict1.get('OR'))

print(dict1.keys())
print(dict1.values())

for key in dict1:
    if key == 'DC':
        print(dict1.get(key))

for key in list(dict1.keys()):
    if key == 'DC':
        del dict1[key]

for key, value in dict1.items():
    print(key, value)

