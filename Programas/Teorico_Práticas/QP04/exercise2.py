def adigits(a, b, c):
    min_1 = min(a, b, c)
    if min_1 == a:
        min_2 = min (b,c)
        min_3 = max (b,c)
    elif min_1 == b:
        min_2 = min (a,c)
        min_3 = max (a,c)
    else:
        min_2 = min (b,a)
        min_3 = max (b,a)
    return int(str(min_1) + str(min_2) +str(min_3))