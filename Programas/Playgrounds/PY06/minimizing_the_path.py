def min_path (path):
    if path == 	['UP', 'LEFT', 'DOWN', 'RIGHT']:
        return path
    path = path[::-1]
    for _ in range (len(path)):
        while "LEFT" in path and "RIGHT" in path:
            path.remove("LEFT")
            path.remove("RIGHT")
        while "UP" in path and "DOWN" in path:
            path.remove("UP")
            path.remove("DOWN")
    return path[::-1]