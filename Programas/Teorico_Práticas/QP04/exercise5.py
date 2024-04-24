def deriv (f):
    def deriv_x(x):
        return round((f(x + 0.001)-f(x))/0.001 , 3)
    return deriv_x