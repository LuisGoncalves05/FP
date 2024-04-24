def search_tree(key, tree, visited = ()):
    if not tree:
        return None
    else:
        visited += (tree[0],)
        if tree[0] == key:
            return (tree[1], list(visited))
        elif key > tree[0]:
            return search_tree(key, tree[3], visited)
        else:
            return search_tree(key, tree[2], visited)