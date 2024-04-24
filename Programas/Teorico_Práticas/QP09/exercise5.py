from functools import reduce

def bounding_box(pts):
    xs = list(map(lambda x: x[0], pts))
    ys = list(map(lambda x: x[1], pts))
    ymin = reduce(min, ys)
    ymax = reduce(max, ys)
    xmin = reduce(min, xs)
    xmax = reduce(max, xs)
    return (xmin,ymin,xmax,ymax)

def max(x, y):
    return x if x > y else y

def min(x, y):
    return x if x < y else y

