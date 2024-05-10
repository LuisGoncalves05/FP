def count_until(tup):
    for _ in tup :
        if type(_) == tuple:
            tup = tup[:tup.index(_)]
            return len(tup)
    else:
        return -1