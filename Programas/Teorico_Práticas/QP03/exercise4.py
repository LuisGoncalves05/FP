while True :
    dimension = int(input())
    if dimension >= 3:
        break

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

if is_even(dimension):
    for _ in range(int(dimension/2 -1)):
        print (dimension*"#")
    for _ in range(2):
        print(int(dimension/2 -1)*"#" + "00" + int(dimension/2 -1)*"#")
    for _ in range(int(dimension/2 -1)):
        print (dimension*"#")
else:
    for _ in range(int((dimension-1)/2)):
        print (dimension*"#")
    print (int((dimension-1)/2)*"#" + "0" + int((dimension-1)/2)*"#")
    for _ in range(int((dimension-1)/2)):
        print (dimension*"#")
    
