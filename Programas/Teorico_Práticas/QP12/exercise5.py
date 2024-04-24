import random

def cows_bulls(seed_value):
    def result(guess):
        random.seed(seed_value)
        correct = random.randint(0, 9999)
        cows = 0
        bulls = 0
        guess = list(str(guess))
        correct = list(str(correct))
        for i in range(len(guess)):
            if guess[i] == correct[i]:
                cows += 1
                guess[i], correct[i] = "a", "b"
        for i in range(len(guess)):
            for j in range(len(guess)):
                if guess[i] == correct[j]:
                    guess[i], correct[j] = "a", "b"
                    bulls += 1
                    break      
        return (cows, bulls)
    return result