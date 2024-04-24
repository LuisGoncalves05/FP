def generator(intlist):
    intlist = map(lambda x: range(x[0], x[1] + 1), intlist)
    new_l = []
    for item in intlist:
        new_l += item
    for item in new_l:
        yield item
