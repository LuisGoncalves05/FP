def bitonic_point(f):
    bitonic_list = f()
    def bitonic_point_list(alist):
        if len(alist) == 1:
            return alist[0]
        ml = alist[:len(alist)//2]
        mr = alist[len(alist)//2:]
        if ml[len(ml)-1] < mr[0]:
            return bitonic_point_list(mr)
        else:
            return bitonic_point_list(ml)
    return bitonic_point_list(bitonic_list)