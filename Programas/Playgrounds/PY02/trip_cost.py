distancia = float(input())
litros_100km = float(input())
preco_litro = float(input())
vezes_percorridos_100km = distancia / 100
litros = litros_100km * (vezes_percorridos_100km)
preco = litros * preco_litro
print(round(preco, ndigits =2))
