def max_path(tree):
    if type(tree) == int:
        return tree
    else:
        tree0 = tree[0]
        tree1 = tree[1]
        tree2 = tree[2]
        return max(max_path(tree0), max_path(tree2)) + tree1