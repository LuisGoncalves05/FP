def repeated_letter(s):
    scpy = list(s)
    s = list(s)
    for char in scpy:
        s.remove(char)
        if char in s:
            return char