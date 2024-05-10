def budgeting(budget, products, wishlist):
    l_wishlist = []
    price = 0
    for product, amount in wishlist.items():
        for _ in range(amount):
            l_wishlist.append((product, products[product]))
            price += products[product]
    l_wishlist.sort(key = lambda x: x[1], reverse = True)

    while price > budget:
        price -= l_wishlist.pop()[1]
    
    new_b = {}
    for product, price in l_wishlist:
        if product in new_b:
            new_b[product] += 1
        else:
            new_b[product] = 1
    
    return new_b