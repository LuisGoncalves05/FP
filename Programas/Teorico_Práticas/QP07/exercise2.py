def roman_to_integer(astring):
    romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    sum = 0
    for let in astring[:len(astring)-1]:
        if romans[let] < romans[astring[astring.index(let) + 1]]:
            astring = astring[1:]
            sum -= romans[let]
        else:
            astring = astring[1:]
            sum += romans[let]
    sum += romans[astring[-1]]
    return(sum)
