stu_id = [1,2,3,4,5]
names = ['Adam', 'Bill', 'Cindy', 'David', 'Ethan']
scores = [7,8,3,6,2]

# for i in range(len(stu_id)):
#     if i == 4:
#         print(stu_id[i], names[i], scores[i])
ind = 0
for index, value in enumerate(names):
    if value == 'Cindy':
        ind = index

print(scores[ind])