def nested_exceptions(tree):
    res = ()
    for item in tree:
        if callable(item):
            try:
                i = item()
                res += (False,)
            except:
                res += (True,)
        else:
            res += (nested_exceptions(item),)
    return res