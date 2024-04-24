def  switch_dict(adict):
    new_dict = {}
    for value in adict.values():
        key_list = []
        for key in adict:
            if value == adict[key]:
                key_list.append(key)
        new_dict.update({value:key_list})
    return(new_dict)