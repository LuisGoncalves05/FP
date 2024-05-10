l = int(input())
s = int(input())
r = l

if r > s:
    pass
else:
    l = r
    r = s
    s = l
while True:
    if s > r:
        if r == 0:
            print(s)
            break
        else:
            l = r
            r = s
            s = l
    else: 
        r = r - s