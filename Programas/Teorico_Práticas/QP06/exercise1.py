def local_minima(alist):
    mins = []
    for i in range(len(alist)-2):
        if calc_loc_min(alist[i:i+3]) == None:
            pass
        else:
            mins.append(calc_loc_min(alist[i:i+3]))
    return (mins)

def calc_loc_min(alist):
    for _ in range(len(alist)):
        if alist.count(min(alist)) > 1:
            return None
        else:
            return (min(alist))
