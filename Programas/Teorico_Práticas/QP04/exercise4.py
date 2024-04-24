def mastermind(g1, g2, g3, c1, c2, c3):
    points = 0
    if g1 == c1:
        points += 3
        c1 = "q"
        g1 = "ç"
    if g2 == c2:
        points += 3
        c2 = "u"
        g2 = "i"
    if g3 == c3:
        points += 3
        c3 = "f"
        g3 = "g"
    if g1 == c2:
        points += 1
        c2 = "e"
        g1 = "r"
    if g1 == c3:
        points += 1
        c3 = "t"
        g1 = "a"
    if g2 == c1:
        points += 1
        c1 = "o"
        g2 = "p"
    if g2 == c3:
        points += 1
        c3 = "s"
        g2 = "d"
    if g3 == c2:
        points += 1
        c2 = "h"
        g3 = "j"
    if g3 == c1:
        points += 1
        c1 = "k"
        g3 = "l"
        
    return(points)