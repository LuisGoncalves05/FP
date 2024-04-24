def mask_data(data, n_characters, position):
    if n_characters == 0:
        return data
    elif n_characters > len(data):
        return "*"*len(data)
    elif position == "end":
        data = data.replace(data[len(data) - n_characters:], n_characters*"*")
    else:
        data = data.replace(data[0:n_characters], n_characters*"*")
    return data

