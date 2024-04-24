def closest_pair(points):
    points = sorted(points)
    if len(points) == 1:
        return False
    if len(points) == 2:
        p1, p2 = points
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
    points_l, points_r = (points[:len(points)//2], points[len(points)//2:])
    dl, dr = (closest_pair(points_l), closest_pair(points_r))
    if not(dl):
        dlr = dr
    elif not(dr):
        dlr = dl
    else:
        dlr = min((dl, dr)) 
    new_dists = []
    for l in points_l:
        for r in points_r:
            dx = abs(l[0]-r[0])
            if dx < dlr:
                new_dists.append(closest_pair((l, r)))
    if new_dists:
        dm = min(new_dists)
        return round(min(dlr, dm))
    else:
        return round(dlr)