def remove_leading(ip):
    split = ip.split(sep=".")
    for num in split:
        if type(num) == int: 
            break
        else:
            i = split.index(num)
            split.insert(i,int(num))
            split.remove(num)
    joined = ""
    for number in split[:len(split)-1]:
        joined += str(number) + "."
    joined += str(split[-1])
    return joined    