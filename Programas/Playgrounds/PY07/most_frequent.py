def most_frequent(alist):
    counts = [alist.count(item) for item in alist]
    max_indexes = [idx for idx in range(len(counts)) if alist.count(alist[idx]) == max(counts)]
    max_numbers = [alist[idx] for idx in max_indexes]
    return max(max_numbers)

