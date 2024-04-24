def mastermind(guesses, codes):
    position = 0
    color = 0
    for i in range(len(guesses)):
        if guesses[i] == codes[i]:
            position += 1
            codes[i] = ""
            guesses[i] = ""
    for i in range(len(guesses)):
        if guesses[i] == "":
            pass
        elif codes.count(guesses[i]) > 0:
            color += 1
            guesses[i] = "frita"
        else:
            pass
    return (position, color)
 	
         