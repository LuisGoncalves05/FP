def four_in_line(board):
    for i in range(len(board)):
        line = board[i]
        for j in range(len(line[:len(line)-3])):
            if line[j] == line[j+1] == line[j+2] == line[j+3]:
                if line[j]:
                    return {(i,j), (i, j+3)}

    for j in range(len(board[0])):
        col = []
        for i in range(len(board)):
            col.append(board[i][j])
        for k in range(len(col[:len(col)-3])):
            if col[k] == col[k+1] == col[k+2] == col[k+3]:
                if col[k]:
                    return {(k,j), (k+3,j)}

    for i in range(len(board)):
        for j in range(len(board[0])):
            if i+3 < len(board) and j+3 < len(board[0]):
                if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                    if board[i][j]:
                        return {(i, j), (i+3, j+3)}
                    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i+3 < len(board) and j-3 >= 0:
                if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]:
                    if board[i][j]:
                        return {(i, j), (i+3, j-3)}

    return {}
