def sparse_dot_product(dict1, dict2):
    if dict1 == {} or dict2 == {}:
        return 0
    v1 = []
    v2 = []
    sum = 0
    for _ in range(max(max(dict1.keys()), max(dict2.keys())) + 1):
        v1.append(0)
        v2.append(0)
    for k, v in dict1.items():
        v1[k] = v
    for k, v in dict2.items():
        v2[k] = v
    for i in range(len(v1)):
        sum += v1[i] * v2[i]
    return(sum)
