def bisect(f, n, lu = (0,1)):
    l, u = lu
    mid = (l + u)/2
    if n == 1:
        return round(mid, 5)
    elif f(mid) > 0 and f(l) > 0 or f(mid) < 0 and f(l) < 0:
        return bisect(f, n-1, (mid, u))
    else:
        return bisect(f, n-1, (l, mid))
