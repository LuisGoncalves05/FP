def triplet(tup):
    for i in tup:
        indexi = tup.index(i)
        tup_modi = tup[indexi+1:]
        if indexi == len(tup) - 3:
            return ()
        for j in tup_modi:
            indexj = tup.index(j)
            tup_modj = tup_modi[indexj+1:]
            for k in tup_modj:
                if i+j+k == 0:
                    return(i,j,k)
