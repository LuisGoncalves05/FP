def discard_middle(s):
    if len(s) <= 3:
        return ""
    new_str = s[:2] + s[-2:]
    return new_str