def fetch_middle(llists):
    list = []
    for item in llists:
        l = len(item)
        if l%2 == 0:
            list.append((item[int(l/2)-1] + item[int(l/2)])/2)
        else:
            list.append(item[int(l/2 - 0.5)])
    return list