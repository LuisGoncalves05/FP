def maximum_depth(l, counter = 1):
    counters = []
    if l != []:
        for item in l:
            counters.append(maximum_depth(item, counter + 1))
    else:
        counters.append(counter)
    return max(counters)