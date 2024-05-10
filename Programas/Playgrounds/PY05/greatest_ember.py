def greatest_member(a_tuple):
    orders = []
    for item in a_tuple:
        if isinstance(item, tuple):
            orders.append(tupledealer(item))
        else:
            order = sum(ord(char) for char in item)
            orders.append(order)
    max_index = orders.index(max(orders))
    return a_tuple[max_index]

def tupledealer(tup):
    orders = []
    for item in tup:
        if isinstance(item, str):
            order = sum(ord(char) for char in item)
            orders.append(order)
        elif isinstance(item, tuple):
            orders.append(tupledealer(item))
        else:
            orders.append(item)
    return sum(orders)
