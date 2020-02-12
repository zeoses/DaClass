def sumMatrix(row, cloum, mat1, mat2):
    '''
    row of matrixs,cloum of matrix, first Matrix, secend Matrix

    '''
    
    result = [[0 for i in range(cloum)] for j in range(row)]

    for i in range(row):
        for j in range(cloum):
            result[i][j] = mat1[i][j] + mat2[i][j]
    

    return result

