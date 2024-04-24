n1 = input()
n2 = input()
n3 = ""

n1_rev = n1[::-1]
n2_rev = n2[::-1]

for _ in range (len(n1)):
    n3 += n1_rev[_]
    n3 += n2_rev[_]

print (n3)

