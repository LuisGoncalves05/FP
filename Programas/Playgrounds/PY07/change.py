def change(money):
    money = money*100
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    counts = []
    for i in range(len(coins)):
        count = 0
        while coins[i] <= money:
            money -= coins[i]
            count += 1
        else:
            counts.append(count)
    change = {round(coin/100, ndigits = 3):count for coin, count in zip(coins, counts)}
    return (change)