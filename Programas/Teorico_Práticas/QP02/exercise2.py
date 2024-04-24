n = input("Qual é o número? ")
n_int = int(n)
milhares = n_int // 1000 * 1000
centenas = (n_int - milhares) // 100 * 100
dezenas = (n_int - milhares - centenas) // 10 * 10
unidades = (n_int - milhares - centenas - dezenas) // 1 
print(str(milhares) +
      "\n" + str(centenas) +
      "\n" + str(dezenas) +
      "\n" + str(unidades))
