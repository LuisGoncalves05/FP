def collatz(n):
    n_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
            n_list.append(n)
        else:
            n = int(n*3 + 1)
            n_list.append(n)
    string = ""
    for i in n_list:
        if i != 1:
            string += str(i) + ","
        else:
            string += str(i)
    return(string)