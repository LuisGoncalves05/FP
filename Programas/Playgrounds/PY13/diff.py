def diff(filename1, filename2):
    with open(filename1) as f1, open(filename2) as f2:
        f1 = f1.readlines()
        f2 = f2.readlines()
        rest1 = f1
        rest2 = f2
        resulting = ""
        while rest1 != rest2 != []:
            rest1, rest2 = eliminate_repeated_beggining(rest1, rest2)
            for idx, line in enumerate(rest1):
                if line in rest2:
                    i1, i2 = (idx, rest2.index(line))
                    missing1 = rest1[:i1]
                    missing2 = rest2[:i2]
                    rest1, rest2 = (rest1[i1:], rest2[i2:])
                    break
            else:
                missing1 = rest1
                missing2 = rest2
                rest1, rest2 = ([], [])
            l = ["- " + i for i in missing1] + ["+ " + i for i in missing2]
            resulting += "".join(l)
        return resulting

def eliminate_repeated_beggining(l1, l2):
    for idx, line1 in enumerate(l1):
            if idx < len(l2) and line1 == l2[idx]:
                pass
            else:
                l1 = l1[idx:]
                l2 = l2[idx:]
                return (l1, l2)