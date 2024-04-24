def bubble_sort(alist):
    flag = True
    while flag:
        flag = False
        for i in range(len(alist) - 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                flag = True
    return alist