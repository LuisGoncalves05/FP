def evaluate(a, x):
    return sum([a[i]*(x**i) for i in range(len(a))])