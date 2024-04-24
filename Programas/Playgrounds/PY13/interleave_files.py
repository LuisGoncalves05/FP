def interleave(f1, f2):
    with open(f1) as f1, open(f2) as f2:
        j = f1.readlines()
        k = f2.readlines()
        l3 = []
        for l1, l2 in zip(j, k):
            joined = l1 + l2
            l3.append(joined)
        return "".join(l3)