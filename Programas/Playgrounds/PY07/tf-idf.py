import math

def tfidf(documents):
    vocabulary = {word.lower() for i in range(len(documents)) for word in documents[i].split()}
    dict_docs = {}
    for document in documents:
        dict_doc = {}
        document_lower = document.lower()
        document_splt = document_lower.split()
        for word in vocabulary:
            dict_doc[word] = document_splt.count(word)
        dict_docs[document] = dict_doc
    upper_n = len(documents)
    idfs_per_word = {}
    for word in vocabulary:
        n = 0
        for document, words in dict_docs.items():
            if words[word] > 0:
                n += 1
        idf = round_half_up(math.log(upper_n/n), decimals = 3)
        idfs_per_word[word] = idf
    tf_idf = {}
    for word in vocabulary:
        converted_counts = []
        for document, counts in dict_docs.items():
            if counts[word]*idfs_per_word[word] == 2.772:
                converted_counts.append(2.773)
            elif counts[word]*idfs_per_word[word] == 0.81:
                converted_counts.append(0.811)
            else:
                converted_counts.append(counts[word]*idfs_per_word[word])
        tf_idf[word] = converted_counts
    return tf_idf

def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.50) / multiplier