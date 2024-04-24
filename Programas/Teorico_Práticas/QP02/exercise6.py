capital_inicial = int(input("Capital: "))
juros = float(input("Juros: "))
frequencia_pagamento = int(input("Frequência de pagamento: "))

capital_final = capital_inicial * (1 + (juros/frequencia_pagamento))**(2*frequencia_pagamento)
print(round(capital_final, ndigits = 3))