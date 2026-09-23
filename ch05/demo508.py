from collections import namedtuple

Car = namedtuple('Car', ['make', 'model'
                         , 'year', 'price'])
honda_accord = Car('Honda', 'Accord', 2026, 26789)
toyota_camry = Car('Toyota', 'Camry', 2022, 29654)
print(honda_accord.price)
print(type(toyota_camry))




