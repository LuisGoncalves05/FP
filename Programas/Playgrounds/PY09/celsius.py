def to_celsius(t):
    fahr = map(lambda x:round((x-32)*(5/9), 2), t)
    return list(fahr)