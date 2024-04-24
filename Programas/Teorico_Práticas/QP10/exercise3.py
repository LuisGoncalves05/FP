def pythagoreans(a, b):
    interval = list(range(a, b))
    return [(a, b, c) for a in interval for b in interval for c in interval if a**2 + b**2 == c**2 and a <= b]
