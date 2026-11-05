import copy

data = ['Adam', 23.65, [5, 'John']]
print(data[2][1])

data0 = data
data1 = data[::] # shallow copy
data2 = data.copy() # shallow copy
data3 = list.copy(data) # shallow copy
data4 = copy.deepcopy(data)
data4[0] = 'Carl'
data4[2][1] = 'David'
print(data[0])
print(data[2][1])