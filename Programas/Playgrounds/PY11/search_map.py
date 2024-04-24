def search_map(map, map_rectangle, search_rectangle):

    def get_coords(start, map_rectangle):
        return ((start[0], start[1], start[0] + map_rectangle[2], start[1] + map_rectangle[3]))
    
    def quadrant_coords(map, map_rectangle, search_rectangle, start = (0, 0), l=[]):
        for idx, item in enumerate(map):
            if idx == 0:
                starting = start
            elif idx == 1:
                starting = (start[0] + map_rectangle[2]/2, start[1])
            elif idx == 2:
                starting = (start[0] + map_rectangle[2]/2, start[1] + map_rectangle[3]/2)
            else:
                starting = (start[0], start[1] + map_rectangle[3]/2)
            if type(item) == str:
                coords = get_coords(starting, map_rectangle[0:2] + (map_rectangle[2]/2, map_rectangle[3]/2))
                l.append((item, coords))
            elif type(item) == tuple:
                quadrant_coords(item, (map_rectangle[0]/2, map_rectangle[1]/2, map_rectangle[2]/2, map_rectangle[3]/2), search_rectangle, starting)
        return l
    
    def coords_in_search(coords, search_rectangle):
        search_rectangle = get_coords(search_rectangle[0:2], search_rectangle)
        xicoord, yicoord, xfcoord, yfcoord = coords
        xisearch, yisearch, xfsearch, yfsearch = search_rectangle
        return not(xisearch > xfcoord or yisearch > yfcoord or xfsearch < xicoord or yfsearch < yicoord)

    coordinates = quadrant_coords(map, map_rectangle, search_rectangle)

    letter_set = set()
    for letter, coords in coordinates:
        if coords_in_search(coords, search_rectangle):
            letter_set.add(letter)
    return letter_set