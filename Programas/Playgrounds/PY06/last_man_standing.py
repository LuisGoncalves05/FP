def last_man_standing(a_list, step):
    idx = -1
    removed = 0
    cpy = a_list.copy()
    while len(cpy) > 1:
        idx += step
        while idx >= len(cpy):
            idx -= len(a_list) - removed
        try:
            cpy.remove(cpy[idx])
            idx -= 1
            removed += 1
        except:
            pass
    return cpy[0]