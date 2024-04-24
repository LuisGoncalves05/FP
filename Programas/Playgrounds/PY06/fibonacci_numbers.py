def fib (n):
    list = [0,1]
    if n == 1: return [0]
    if n == 2: return list
    for _ in range (int(n)-2):
        list.append(list[-1] + list[-2])
    return list