def pattern_hunting(l1, l2, p):
    indexes1 = []
    for index in range(len(l1)):
        if p in l1[index]:
            indexes1.append(index)
    indexes2 = []
    for index in range(len(l2)):
        if p in l2[index]:
            indexes2.append(index)
    l3 = [l1[index] for index in indexes2]
    l4 = [l2[index] for index in indexes1]
    return l3 + l4