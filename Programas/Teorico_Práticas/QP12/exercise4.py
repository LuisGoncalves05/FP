def move_ball(board):
    path = []
    directions = ['W', 'N', 'E', 'S']
    list_board = []
    for line in board:
        list_line = []
        for char in line:
                list_line.append(char) 
        list_board.append(list_line)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                end = (i, j)
            elif board[i][j] in directions:
                start = (i, j)
                direction = board[i][j]
    path.append(start)
    while path[-1] != end:
        current = path[-1]
        if direction == "N":
            next = (current[0] - 1 , current[1])
        elif direction == "S":
            next = (current[0] + 1 , current[1])
        elif direction == "E":
            next = (current[0] , current[1] + 1)
        else:
            next = (current[0] , current[1] - 1)
        path.append(next)
        from_l = current[1] < next[1]
        from_r = current[1] > next[1]
        from_up = current[0] < next[0]
        from_down = current[0] > next[0]
        if board[next[0]][next[1]] == "/":
            if from_down or from_up:
                idx = (directions.index(direction) + 1) % len(directions)
            else:
                idx = directions.index(direction) -1
            direction = directions[idx]
        elif board[next[0]][next[1]] == "\\":
            if from_down or from_up:
                idx = directions.index(direction) - 1
            else:
                idx = (directions.index(direction) + 1) % len(directions)
            direction = directions[idx]
    return path