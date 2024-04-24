def preorder(tree, l = []):
    if tree:
        l.append(tree[0])
        preorder(tree[1], l)
        preorder(tree[2], l)
    return l