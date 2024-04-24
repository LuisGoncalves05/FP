def budgeting(money, products, wishlist, bought = dict()):
    if wishlist == dict(): return dict()

    product, wishlist = choose(wishlist)
    a = budgeting(money, products, wishlist, bought)
    try:
        money, bought = buy(money, products, product, bought)
        b = budgeting(money, products, wishlist, bought)
        avalue = evaluate(a)
        bvalue = evaluate(b)
        return a if avalue > bvalue else b
    except:
        return a

def evaluate(products, bought):
    result = 0
    for product in bought:
        result += bought[product] * products[product]
    return result

def choose(wishlist):
    """
    Choose next item to buy. Returns (product, wishlist)
    """
    product = list(wishlist.keys())[0]
    wishlist[product] -= 1
    if not wishlist[product]: del wishlist[product]
    return (product, wishlist)

def buy(money, products, product, bought):
    """
    Buys an item and updates the money. Returns a tuple with (money, bought)
    """
    if money < products[product]: raise ValueError

    money -= products[product]
    bought = bought.copy()
    bought[product] = bought.get(product, 0) + 1

    return (money, bought)

print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40, 'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))