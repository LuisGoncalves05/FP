def bagdiff(xs, ys):
    for item in ys:
        if item in xs:
            xs.remove(item)
    return xs