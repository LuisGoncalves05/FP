def rearrange(l):
    pos = list(filter(lambda x: x>0, l))
    neg = list(filter(lambda x: x<=0, l))
    return neg + pos