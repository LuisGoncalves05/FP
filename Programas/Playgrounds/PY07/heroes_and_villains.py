def fight(heroes, villain):
    for hero in heroes:
        if hero["category"] == villain["category"]:
            if hero["health"] >= villain["health"]:
                hero["score"] += 1
                villain["health"] = 0
                return(f"{hero['name']} defeated the villain and now has a score of {hero['score']}")
            else:
                villain["health"] -= hero["health"]/2
    if villain["health"] > 0:
        return(f"{villain['name']} prevailed with {villain['health']}HP left")
