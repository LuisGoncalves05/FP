def magic(mat):
    sum_list = []
    for line in range(len(mat)):
        line_sum = 0
        for element in range(len(mat[line])):
            line_sum += mat[line][element]
        sum_list.append(line_sum)
    for column in range(len(mat)):
        column_sum = 0
        for element in range(len(mat)):
            column_sum += mat[element][column]
        sum_list.append(column_sum)
    diag_1_sum = 0
    diag_2_sum = 0    
    for index in range(len(mat)):
        diag_1_sum += mat[index][index]
        diag_2_sum += mat[index][(len(mat)-1) - index]
    sum_list.append(diag_1_sum)
    sum_list.append(diag_2_sum)
    for sum in sum_list:
        if sum != sum_list[sum_list.index(sum) - 1]:
            return False
    return True

