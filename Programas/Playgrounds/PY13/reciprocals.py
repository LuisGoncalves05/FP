def reciprocals(alist):
    return [1/x for x in alist if (type(x) == int or type(x) == float) and x != 0]