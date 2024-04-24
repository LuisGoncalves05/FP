def permuta(alist, step=0, all=[]):
    if len(alist) == 1:
        return [alist]
    else:
        for i in range(len(alist)):
            if i >= step:
                workable = alist.copy()
                workable[step], workable[i] = workable[i], workable[step]
                if workable not in all:
                    all.append(workable)
                permuta(workable, step +1, all)
    return all