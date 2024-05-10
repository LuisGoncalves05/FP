a = int(input())
b = int(input())
um_par_dois_impar = (a+b) % 2 + 1
print((um_par_dois_impar%2 + 1)*(a+b) + (um_par_dois_impar - 1)*(a*b))
