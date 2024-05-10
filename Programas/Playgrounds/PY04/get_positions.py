def get_positions(sentence, word_list):
    index_list = []
    sentence = sentence.split()
    for word in sentence:
        if word in word_list:
            word_index = word_list.index(word)
            index_list.append(word_index)
        else:
            return ""
    index_string = ""
    for i in index_list:
        index_string += str(i) + " "
    return index_string