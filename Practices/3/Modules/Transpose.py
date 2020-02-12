def TransposeMatrix(row, cloum, mat1):

    result = [[0 for i in range(row)] for j in range(cloum)]

    for i in range(row):
        for j in range(cloum):
            result[j][i] = mat1[i][j] 
    

    return result