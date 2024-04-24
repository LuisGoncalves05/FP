def get_composites(n):
    for comp in range(4, n+1):
        for test in range(2,comp):
            if comp % test == 0:
                yield comp
                break