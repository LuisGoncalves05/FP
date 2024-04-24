def permutations(atuple):
    atuple = tuple(atuple)
    if len(atuple) == 1:
        return{atuple}
    elif len(atuple) == 2:
        return{(atuple[0], atuple[1]), (atuple[1], atuple[0])}
    else:
        perms = permutations(atuple[1:])
        s = set()
        for i in range (len(atuple)):
            for perm in perms:
                s.add(perm[:i] + (atuple[0],) + perm[i:])
        return s