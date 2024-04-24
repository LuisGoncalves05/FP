def permutations(stri):
    if stri == "" or len(stri) == 1:
        return [stri]
    elif len(stri) == 2:
        perms = [stri, stri[1] + stri[0]]
    else:
        perms = permutations(stri[1:])
        new_p = perms.copy()
        perms = []
        for perm in new_p:
            perm = [letter for letter in perm]
            for i in range(len(perm) + 1):
                perm.insert(i, stri[0])
                perms.append("".join(perm))
                perm.remove(stri[0])
    return perms
