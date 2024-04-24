def to_fahrenheit(t):
    cel = map(lambda x:round(x*(9/5) + 32, 2), t)
    return list(cel)