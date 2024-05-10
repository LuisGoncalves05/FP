def solver(a,b,c):
    result1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    result2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    if (b**2-4*a*c) < 0:
        return([])
    elif result1 == result2:
        return([result1])
    else:
        return(sorted([result1, result2]))