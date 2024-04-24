def variance(alist):
    n = len(alist)
    med = sum(alist)/n
    meds = [med] * n
    var = sum(map(lambda x, y: (x -y)**2  ,alist, meds))/n
    return round(var, 3)
