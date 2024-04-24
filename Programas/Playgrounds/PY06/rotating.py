def rotate_list(l):
    cpy = l.copy()
    l = l[3:]
    l.extend(cpy[0:3])
    return l