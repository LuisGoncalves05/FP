def differences(alist):
    return list(map(lambda x: x[1] - x[0], zip(alist, alist[1:])))