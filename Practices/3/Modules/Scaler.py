def ScalerMatrix(row, cloum, mat1, num):
    '''
    row of matrixs,cloum of matrix, A Matrix, Num

    '''
    
    result = [[0 for i in range(cloum)] for j in range(row)]

    for i in range(row):
        for j in range(cloum):
            result[i][j] = mat1[i][j] * num
    

    return result

