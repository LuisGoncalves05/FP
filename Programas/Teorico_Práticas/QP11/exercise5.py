def longest_prefix(words):
    if len(words) == 1:
        return words[0]
    elif len(words) == 2:
        w0, w1 = words[0], words[1]
        while w0 != w1:
            if len(w0) > len(w1):
                w0 = w0[:len(w0)-1]
            elif len(w0) < len(w1):
                w1 = w1[:len(w1)-1]
            else:
                w0 = w0[:len(w0)-1]
                w1 = w1[:len(w1)-1]
        return w0
    else:
        wl = words[:len(words)//2]
        wr = words[len(words)//2:]
        return longest_prefix([longest_prefix(wl), longest_prefix(wr)])