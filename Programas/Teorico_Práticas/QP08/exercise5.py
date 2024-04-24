def soup(matrix, word):
    for line in range(len(matrix)):
        for col in range(len(matrix[0])):
            if word == "":
                return None
            if matrix[line][col] == word[0]:
                word_found = soup_rec(matrix, word[1:], line, col)
                if word_found:
                    return chr(65 + line) + str(col+1)

def soup_rec(matrix, word, line, col):
    if word == "":
        return True
    combs = {(a, b) for a in range(-1,2) for b in range(-1,2) if abs(a) != abs(b)}
    for comb in combs:
        new_l = line + comb[0]
        new_col = col + comb[1]
        if 0 <= new_l < len(matrix):
            if 0 <= new_col < len(matrix[0]):
                if word[0] == matrix[new_l][new_col]:
                    return soup_rec(matrix, word[1:], new_l, new_col)
    return False