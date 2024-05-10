n_oct = input()
n_dec = 0
l = len(n_oct)
exponents = range (l, -1, -1)

for _ in range(l, 0, -1):
    n_dec += int(n_oct[_-1]) * 8**(exponents[_])

for i in n_oct:
    if int(i) >= 8:
        print("Not a valid number.")
        break
else:
    print(n_dec)