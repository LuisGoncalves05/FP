def x_union(list1, list2):
    list1_firsts = list(map(lambda x: x[0], list1))
    list2_firsts = list(map(lambda x: x[0], list2))
    list1_filtered = list(filter(lambda x: x not in list2_firsts, list1_firsts))
    list2_filtered = list(filter(lambda x: x not in list1_firsts, list2_firsts))
    list1 = list(filter(lambda x: x[0] in list1_filtered, list1))
    list2 = list(filter(lambda x: x[0] in list2_filtered, list2))
    return list1 + list2
