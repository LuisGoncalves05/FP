def square_odds(value):
    lst = value.split(",")
    lst = [str(int(x)**2) for x in lst if int(x) % 2 != 0]
    return ",".join(lst)
