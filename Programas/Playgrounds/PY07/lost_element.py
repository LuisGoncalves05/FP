def lost_element(s1, s2):
    return(list((s1-s2)|(s2-s1))[0])