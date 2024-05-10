def C(n, r):
    num = factorial(n)
    den = factorial(r) * factorial(n-r)
    return(num/den)

def factorial(x):
    prod = 1
    for i in range(1, x+1):
        prod *= i
    return prod