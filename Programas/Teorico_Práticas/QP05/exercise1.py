def rm_letter_rev(ch, s):
    s = s[::-1]
    if ch in s:
        s = s.replace(ch, "")
    return s