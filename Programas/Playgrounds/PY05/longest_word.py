def longest(s):
    spl = s.split()
    len_word = []
    for word in spl:
        len_word.append(len(word))
    return max(len_word)
        