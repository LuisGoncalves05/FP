n = int(input())
interval = [0.0, n]
while True:
    midpoint = (interval[0] + interval[1])/2
    if midpoint*midpoint == n or abs(interval[0]-interval[1]) < 0.00001:
        print (round(midpoint, ndigits = 5))
        break
    elif midpoint*midpoint > n:
        interval[1] = midpoint
    else:
        interval[0] = midpoint