a = int(input())
b = int(input())
c = int(input())
solution1 = round((-b + (b**2-4*a*c)**0.5)/(2*a), ndigits = 2)
solution2 = round((-b - (b**2-4*a*c)**0.5)/(2*a), ndigits = 2)
print("The solutions are", solution1, "and", solution2)