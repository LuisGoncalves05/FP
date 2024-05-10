def is_looping ():
    n = input()
    l = len(n)
    list = []
    for _ in n:
        list.append(int(_))
    for i in range (1, l):
        if abs(list[i] - list[i-1]) == 1 or abs(list[i] - list[i-1]) == 9:
            pass
        else: 
            return False
    else:
        return True
    
if is_looping():
    print ("Looping number")
else: 
    print("Not a looping number")