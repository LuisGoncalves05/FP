lista = []
total = 0
n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        lista.append(i)
    else:
        pass

for i in lista:
    total += i

print(total)