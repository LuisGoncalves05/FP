LE = int(input())
RE = int(input())
PE = int(input())
TE = int(input())
grade = (LE + RE + 13 * PE + 5 * TE) / 100
if not(0<=LE<=100) or not(0<=RE<=100) or not(0<=PE<=100) or not(0<=TE<=100):
    print ("Input error")
elif PE < 40 or TE < 40:
    print ("RFF")
else:
    print(round(grade))