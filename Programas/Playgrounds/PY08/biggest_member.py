def biggest_member(atuple, lens = []):
    if type(atuple) == tuple:
        lens += [(len(atuple), atuple)]
    for item in atuple:
        if type(item) == tuple:
            biggest_member(item, lens)
    lens.sort()
    return lens[-1][1]
