def palindrome_index(s):
    slist = []
    for letter in s:
        slist.append(letter)
    slist_rev = slist.copy()[::-1]
    if "".join(slist) == "".join(slist_rev):
        return -1
    for letter in s:
        r = slist.copy()
        sl = slist.copy()
        sl.remove(letter)
        r.remove(letter)
        r = r[::-1]
        if r == sl:
            return s.index(letter)
    else:
        return -1