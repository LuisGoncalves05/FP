import math

def order(n):
    counter = 0
    while n > 10:
        counter += 1
        n = n//10
    return counter +1

def digits_average(n):
    if n < 10:
        return n
    ord = order(n)
    new = 0
    for dif_orders in range(1, ord):
        n1 = n % (10**dif_orders) // 10**(dif_orders-1)
        n2 = (n % (10**(dif_orders+1)) - n1) // 10**dif_orders
        a = math.ceil((n1+ n2)/2)
        new += a*10**(dif_orders-1)
    return digits_average(new)