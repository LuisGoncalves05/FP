from math import ceil

def avg(a, b):
    return ceil((a+b)/2)

def digits_average(n, acc = 0, power = 0):
    if n < 10:
        return n
    elif n < 100:
        return acc + avg(n//10, n%10) * 10**power
    else:
        n_except_last = n//10 
        n_last_2 = n % 100
        acc += avg(n_last_2//10, n_last_2%10) * 10**power
        power += 1
        acc = digits_average(n_except_last, acc, power)
        return digits_average(acc)