def four_in_line(board):
    for i in range(len(board)):
        line = board[i]
        for j in range(len(line) - 3):
            start = (i, j, line[j])
            if start[2] != 0:
                for k in range(1, 4):
                    if line[j+k] == start[2]:
                        end = (i, j+3)
                    else:
                        start= ()
                        break
                if start:
                    return {start[:2], end}
    for j in range(len(board[0])):
        column = []
        for i in range(len(board)):
            column.append(board[i][j])
        for l in range(len(column) - 3):
            start = (l, j, column[l])
            if start[2] != 0:
                for m in range(1, 4):
                    if column[l+m] == start[2]:
                        end = (l+3, j)
                    else:
                        start = ()
                        break
                if start:
                    return {start[:2], end}
    for i in [(2,1,4), (1,0,5), (0,0,5), (0,1,4)]:
        diag = []
        for j in range(i[2]):
            diag.append(board[i[0]+j][i[1]+j])
        if len(diag)==4:
            if diag in [[1]*4, [2]*4]:
                return {i[0:2], (i[0]+3, i[1]+3)}
        else:
            diag1 = diag[:4]
            diag2 = diag[1:]
            if diag1 in [[1]*4, [2]*4]:
                return {i[0:2], (i[0]+3, i[1]+3)}
            elif diag2 in [[1]*4, [2]*4]:
                return {(i[0]+1, i[1]+1), (i[0]+4, i[1]+4)}
    return set()

print(four_in_line([[0, 2, 0, 0, 0], [0, 2, 2, 0, 0], [0, 2, 2, 2, 1], [0, 1, 1, 1, 2], [0, 1, 1, 2, 2]]))
