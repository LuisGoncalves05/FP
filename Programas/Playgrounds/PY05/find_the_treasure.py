def map(pos, steps):
    x, y = pos
    spl = steps.split(sep = "-")
    u = spl.count("up")
    d = spl.count("down")
    l = spl.count("left")
    r = spl.count("right")
    x += l*(-1) + r*1
    y += d*(-1) + u*1
    return(x,y)