def multi(g):
    repeat = 0
    length_initial = len(g)
    for tuple in g:
        count = g.count(tuple)
        index = g.index(tuple)
        while True:
            if tuple in g[index+1:]:
                repeat += 1
                index2 = index + 1 + g[index+1:].index(tuple)
                g = (g[:index2] + g[index2+1:])
            else:
                break
        tuple = (tuple[0], count, tuple[1])
        if index != 0:
            g = ((tuple,) +g[:index] + g[index+1:])
        else:
            g = ((tuple,) + g[1:])
        if index + 1 + repeat == length_initial:
                break
    return g
