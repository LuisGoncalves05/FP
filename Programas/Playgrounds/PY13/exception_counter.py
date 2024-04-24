def count_exceptions(f, n1, n2):
    counter = 0
    for i in range(n1, n2 + 1):
        try:
            f(i)
        except:
            counter += 1
    return counter