def sum_digits_rec(n):
    if len(str(n)) > 1:
        dig = int(str(n)[0])
        n = int(str(n)[1:])
        return dig + sum_digits_rec(n)
    return n
