def number_of_collisions(objects):
    cols = 0
    pairs = [(item1, item2) for item1 in objects for item2 in objects[objects.index(item1):] if item1 != item2]
    for pair in pairs:
        o1 = pair[0]
        o2 = pair[1]
        if o1["x1"] > o2["x2"] or o1["x2"] < o2["x1"]:
            pass
        elif o1["y1"] > o2["y2"] or o1["y2"] < o2["y1"]:
            pass
        else:
            cols += 1
    return cols