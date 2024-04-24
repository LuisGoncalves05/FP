def longest(filename):
    with open(filename, "r") as file:
        l = file.read()
        l = l.split()
        counts = []
        for word in l:
            counts.append(len(word))
        return l[counts.index(max(counts))]