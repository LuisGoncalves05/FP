def summary_ranges(a_string):
    splt = a_string.split(sep=",")
    splt = [int(num) for num in splt]
    ranges = []
    i = 0
    while i < len(splt):
        start = splt[i]
        while i+1 < len(splt) and splt[i+1] - splt[i] == 1:
            i += 1
        end = splt[i]
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{end}")
        i += 1
    ranges = ",".join(ranges)
    return ranges