def division(a, b):
    if b == 0:
        return("can't divide by 0!")
    elif not check(a, b):
        return("unsupported operand type(s) for division")
    else:
        return f"{a}/{b} = {a/b}"
    
def check(a, b):
    return (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float)