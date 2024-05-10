n = int(input())

for _ in range(n):
    for i in range(n-1, -1, -1):
        print (i+1, "", end = "")
    n -=1
    print()