def transitive_closure(r, acc = 0):
    if acc != len(r):
        r.update({rel_composition(r1, r2) for r1 in r for r2 in r if rel_composition(r1, r2)})
        acc += 1
        transitive_closure(r, acc)
    return r
    
def rel_composition(r1, r2):
    return (r1[0], r2[1]) if r1[1] == r2[0] else ()