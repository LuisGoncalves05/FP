def change(amount):
    poss_change = [200, 100, 50, 20, 10, 5, 2, 1]
    real_change = []
    for money in poss_change:
        if amount == 0:
            break
        while True:
            if (amount - money) >= 0:
                real_change.append(money)
                amount -= money
            else:
                break
    return real_change

