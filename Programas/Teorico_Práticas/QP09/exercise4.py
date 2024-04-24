from functools import reduce

def dec2int(alist):
    return reduce(lambda x, y: x*10 + y ,alist)

