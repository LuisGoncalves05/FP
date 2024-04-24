def no_consecutives1(k, counted = 0, good = 0):
    total = 2**k
    if counted >= total:
        return good
    if "11"  not in f"{counted:{k}b}":
        counted += 1
        good += 1
    else:
        counted += 1
    return no_consecutives1(k, counted, good)