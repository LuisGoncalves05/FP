import math

def row(n):
    single_row = ""
    for i in range (n+1):
        single_row += str(int(((math.factorial(n)/(math.factorial(i)*math.factorial(n-i)))))) 
        if i < n:
                single_row += " "
    return single_row

def pascal(n):
    rows = ""
    for i in range(n):
        rows += (str(row(i)) + "\n")
    return rows
