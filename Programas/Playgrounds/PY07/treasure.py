def treasure(clues):
    clues = dict(clues)
    if (0,0) not in clues:
        return ()
    else:
        init = clues[(0,0)]
        del clues[(0,0)]
    while init in clues:
        temp = clues[init]
        del clues[init]
        init = temp
    return init
    
