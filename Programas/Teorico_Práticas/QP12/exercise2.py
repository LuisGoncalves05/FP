def tic_tac_toe(board, player):
    new_board = [[], [], []]
    for i in range(3):
        for j in range(3):
            col_num = i + j + 3*i
            new_board[i].append(board[col_num])
    for i in range(3):
        for j in range(3):
            if new_board[i][j] == " ":
                coord = f"{chr(ord('A') + i)}{j + 1}"
                new_board[i][j] = player
                if is_winner(new_board, player):
                    return coord
                new_board[i][j] = " "

def is_winner(board, player):
    diag = [board[i][i] for i in range(3)]
    antidiag = [board[2-i][i] for i in range(3)]
    w = [player]*3
    cols = []
    for j in range(3):
        cols.append([board[i][j] for i in range(3)])
    for k in range(3):
        if board[k] == w or cols[k] == w or diag == w or antidiag == w:
            return True