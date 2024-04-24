def solve_sudoku(board):
    lines = []
    cols = []
    for i in range(len(board)):
        lines.append(board[i])
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        cols.append(col)

    new_board = [l[:] for l in board]
    for i in range(len(new_board)):
        for j in range(len(new_board)):
            if new_board[i][j] == 0:
                for k in range(1, 10):
                    if not(k in board[i] or k in cols[j]):
                        new_board[i][j] = k
                        while not_bad(new_board):
                            new_board = solve_sudoku(new_board)
                        else:
                            new_board[i][j] = 0
                return None

def not_bad(board):
    lines = []
    cols = []
    #subgrids = []
    if board:
        for i in range(len(board)):
            lines.append(board[i])
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
            cols.append(col)
        for line in lines:
            if sorted(line) != sorted(list(set(line))):
                return False
        for col in cols:
            if sorted(col) != sorted(list(set(col))):
                return False
        #for i in range(3):
            #for j in range(3):

        return True
    else:
        return False

def good(board):
    lines = []
    cols = []
    for i in range(len(board)):
        lines.append(board[i])
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        cols.append(col)
    good_l_c = [i for i in range(1,10)]
    for line in lines:
        if sorted(line) != good_l_c:
            return False
    for col in cols:
        if sorted(col) != good_l_c:
            return False
    return True










def solve_sudoku(board):
    lines = []
    cols = []
    for i in range(len(board)):
        lines.append(board[i])
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        cols.append(col)

    new_board = [l[:] for l in board]
    for i in range(len(new_board)):
        for j in range(len(new_board)):
            if new_board[i][j] == 0:
                for k in range(1, 10):
                    if not(k in board[i] or k in cols[j]):
                        new_board[i][j] = k
                        new_board = solve_sudoku(new_board)
    if good(new_board): return new_board 

def good(board):
    lines = []
    cols = []
    for i in range(len(board)):
        lines.append(board[i])
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        cols.append(col)
    good_l_c = [i for i in range(1,10)]
    for line in lines:
        if sorted(line) != good_l_c:
            return False
    for col in cols:
        if sorted(col) != good_l_c:
            return False
    return True