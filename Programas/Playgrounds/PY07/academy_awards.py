def academy_awards(alist):
    movies = list({alist[i][1] for i in range(len(alist)) if alist[i][1]})
    final = {}
    for movie in movies:
        counter = 0
        for i in range(len(alist)):
            if movie == alist[i][1]:
                counter += 1
        final[movie] = counter
    return final
