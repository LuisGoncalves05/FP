def evaluate(a, x):
    b = list(enumerate(a))
    values = map(lambda k:k[1]*(x**k[0]), b)
    return sum(values)