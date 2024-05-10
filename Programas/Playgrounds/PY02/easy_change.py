preco = int(input())
recebido = int(input())
troco = recebido - preco
cinquenta = troco // 50
vinte = troco % 50 // 20
dez = troco % 50 % 20 // 10
cinco = troco % 50 % 20 % 10 // 5
print (cinquenta, vinte, dez, cinco)