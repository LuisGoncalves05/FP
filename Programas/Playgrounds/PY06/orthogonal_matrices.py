def is_orthogonal(mx):
    order = len(mx)
    identity = []
    transposed = []
    for line in range(order):
        l = [0] * order
        l[line] = 1
        identity.append(l)
    for column in range(order):
        col = []
        for l in mx:
            col.append(l[column])
        transposed.append(col)
    return mx_sq_prod(mx, transposed) == identity

def mx_sq_prod(mx1, mx2):
    mx3 = []
    order = len(mx1)
    cols = []
    for column in range(order):
        col = []
        for line in mx2:
            col.append(line[column])
        cols.append(col)
    for line in mx1:
        l = []
        for col in cols:
            product = 0
            for i in range(order):
                product += line[i]*col[i]
            l.append(product)
        mx3.append(l)
    return mx3