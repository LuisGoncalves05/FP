import string

def complete_pairs(s1, s2):
    letters = string.ascii_lowercase
    combinations = set()
    combinations_2_remove = set()
    for item1 in s1:
        for item2 in s2:
            comb1 = item1 + item2
            combinations.add(comb1)
    for combination in combinations:
        for letter in letters:
            if letter not in combination:
                combinations_2_remove.add(combination)
                break
            else:
                pass
    return combinations - combinations_2_remove

print(complete_pairs({'abc', 'geeksforgeeks', 'abcdefgh', 'lmnopqrst'}, {'defghijklmnopqrstuvwxyz', 'ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'}))