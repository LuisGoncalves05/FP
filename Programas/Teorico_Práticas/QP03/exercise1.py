num = int(input())

for _ in range (10):
    if _+1 != num:
        print (f"{num} x {_+1} = {num * (_+1)}")
    else: 
        print(f"{num} ^ 2 = {num**2}")
        break