def sort_by_value(dict):
    l = list(dict.items())
    l_rev = [(v,k) for k,v in l]
    l_rev_sorted = sorted(l_rev)
    l_sorted = [(v,k) for k,v in l_rev_sorted]
    return l_sorted
