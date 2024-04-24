def mult(M, N):
    product = []
    if len(M[0]) != len(N):
        return []
    else:
        for lm_cn in range(len(M)):
            line_m = M[lm_cn]
            line_final = []
            for cm_ln in range(len(N[0])):
                col_n =[]
                for i in range(len(N)):
                    col_n += [N[i][cm_ln]]
                multiplied = 0
                for m, n in zip(line_m, col_n):
                    multiplied += m * n
                line_final.append(multiplied)
            product.append(line_final)
    return product

