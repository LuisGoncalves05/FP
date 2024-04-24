def paint(n, boards):
    combinations = get_combs(n, boards)
    times = [sum([max(i) for i in combinations[j]]) for j in range(len(combinations))]
    return min(times)

def get_combs(n, boards):
    if n == 1:
        return [[boards]]
    elif n == 2:
        return [[boards[:i], boards[i:]] for i in range(1, len(boards))]
    else:
        result = []
        for i in range(1, len(boards)):
            part1 = get_combs(n//2, boards[:i])
            part2 = get_combs(n-n//2, boards[i:])
            for i in [j + k for j in part1 for k in part2]:
                result.append(i) 
        return result