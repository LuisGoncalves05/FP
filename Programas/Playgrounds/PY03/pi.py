import math

k = 50
factor = 2*(2**(0.5))/9801
sum = 0

for k in range (k+1):
    sum = sum + (math.factorial(4*k)*(1103 + 26390*k)) / ((math.factorial(k) ** 4) * 396 ** (4*k))

pi_inverse = factor * sum
pi = pi_inverse ** -1
print(round(pi, ndigits=8))