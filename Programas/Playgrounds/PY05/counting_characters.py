def count_chars(a_string):
    alpha = 0
    dig = 0
    spec = 0
    for char in a_string:
        if char.isdigit():
            dig += 1
        elif char.isalpha():
            alpha += 1
        else:
            spec += 1
    return(alpha, dig, spec)

print(count_chars('Str1nG$'))