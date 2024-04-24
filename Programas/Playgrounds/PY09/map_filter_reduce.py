from functools import reduce

def map_filter_reduce(lst, f1, f2, f3):
    filtered = list(filter(f1, lst))
    applied_f2 = [f2(i) for i in filtered]
    return reduce(f3, applied_f2)