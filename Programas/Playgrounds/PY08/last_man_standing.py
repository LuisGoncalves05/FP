def last_man_standing(alist, step, idx = -1):
    idx += step
    l = len(alist)
    idx = idx_corrector(idx, l)
    if l != 1:
        del alist[idx]
        idx -= 1
        last_man_standing(alist, step, idx,)
    return alist[0]

def idx_corrector(idx, l):
    if idx > l - 1: 
        return idx_corrector(idx - l, l)
    if idx == -1:
        idx = l-1
    return idx
