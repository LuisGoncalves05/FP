def juggler(n, p):
    if n >= 0 and p >= 0:
        if p == 0:
            return n
        elif juggler(n, p-1) % 2 == 0:
            return int(juggler(n, p-1)**(1/2))
        else:
            return int(juggler(n, p-1)**(3/2))
    else:
        return 0