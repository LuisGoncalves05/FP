def union_with(combine, dict1, dict2):
    repeated = {key1:combine(dict1[key1], dict2[key2]) for key1 in dict1 for key2 in dict2 if key1 == key2}
    dict1_clean = {key:value for key, value in dict1.items() if key not in repeated}
    dict2_clean = {key:value for key, value in dict2.items() if key not in repeated}
    sum = dict()
    sum.update(dict1_clean)
    sum.update(dict2_clean)
    sum.update(repeated)
    return sum