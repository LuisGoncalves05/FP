def find_me(f, limits, count = 0):
    mid = (limits[0] + limits[1])//2 
    count += 1
    if f(mid) == -1:
        return find_me(f, (limits[0], mid-1), count)
    elif f(mid) == 1:
        return find_me(f, (mid+1, limits[1]), count)
    else:
        return count