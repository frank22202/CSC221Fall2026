def avg_score(*args, **kwargs):
    print(kwargs['name'], kwargs['score'])
    print(args)
    print(type(args))
    return sum(args) / len(args)

# print(avg_score(99, 88, 73, 100, 81))
avg_score(99, 87, name='John', score=96)