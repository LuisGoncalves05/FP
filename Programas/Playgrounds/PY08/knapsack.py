def knapsack(money, products, wishlist):
    combs = get_combs(money, products, wishlist, {})
    optimal = 0
    for i in range(len(combs[1:])):
        if combs[optimal][0] > combs[i][0]:
            optimal = i
    return combs[optimal][1]

def get_combs(money, products, wishlist, bought) -> list:
    combs = []

    for product in wishlist:
        new_w = wishlist.copy()
        if new_w[product] == 1:
            new_w.pop(product)
        else:
            new_w[product] -= 1

        new_b = bought.copy()
        if product in new_b:
            new_b[product] += 1
        else:
            new_b[product] = 1

        new_m = money - products[product]

        if new_m >= 0:
            combs.append((new_m, new_b))
        if new_m > 0:
            combs += get_combs(new_m, products, new_w, new_b)
    return combs