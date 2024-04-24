def count_zeros(f):
    int_l = f()
    def list_div(alist):
        alistl = alist[:len(alist)//2]
        alistr = alist[len(alist)//2:]
        if 1 in alistr:
            return list_div(alistr)
        elif 0 in alistl:
            return len(alistr) + list_div(alistl)
        else:
            return len(alistr)
    return list_div(int_l)