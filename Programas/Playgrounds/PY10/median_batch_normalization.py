def batch_norm(alist, batch_size):
    l_of_ls = []
    for _ in range(int(len(alist)/batch_size)):
        l_of_ls.append([])
    for i in range(len(l_of_ls)):
        l = l_of_ls[i]
        counter = 0
        for item in alist[i*batch_size:(i+1)*batch_size]:
            if counter < batch_size:
                l.append(item)
                counter += 1
    if len(alist) % batch_size != 0:
        l_of_ls.append(alist[(len(alist) // batch_size)*batch_size:])
    for l in l_of_ls:
        med = median(l)
        for i in range(len(l)):
            l[i] -= med
        yield l


def median(alist):
    alist = sorted(alist)
    if len(alist) % 2 == 0:
        return (alist[int(len(alist)/2) -1] + alist[int(len(alist)/2)])/2
    else:
        return alist[len(alist)//2]
    
print(list(batch_norm([2, 4, 6], 2)))