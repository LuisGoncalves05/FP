def comprehensions(i, j):
    interval = list(range(i, j+1))
    p1 = [x for x in interval if x%10 == 3 or x%10 == 8]
    p2 = tuple((round(x**0.5, 2)for x in interval))
    p3 = {x: chr(x) for x in interval}
    return (p1, p2, p3)