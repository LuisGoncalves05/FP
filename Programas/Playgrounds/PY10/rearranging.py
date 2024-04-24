def rearrange(l):
    pos = [x for x in l if x > 0]
    neg = [x for x in l if x <= 0]
    return neg + pos