def solve(matrix: list):
    for i in range(len(matrix)):
        if matrix[i][0]>matrix[0][0]:
            matrix[i], matrix[0] = matrix[0], matrix[i]
    for i in range(1, len(matrix)):
        d = round((matrix[i][0]/matrix[0][0]), 6)
        for j in range(len(matrix[i])):
            matrix[i][j] = round((matrix[i][j] - d*matrix[0][j]), 6)
    if matrix[1][1]==0:
        matrix[2], matrix[1] = matrix[1], matrix[2]
    else:
        if matrix[2][1]>matrix[1][1]:
            matrix[1], matrix[2] = matrix[2], matrix[1]
        d = round((matrix[2][1]/matrix[1][1]), 6)
        for j in range(1, len(matrix[2])):
            matrix[2][j] = round((matrix[2][j]-d*matrix[1][j]), 6)
    x3 = round(matrix[2][3] / matrix[2][2], 5)
    x2 = round(((matrix[1][3] - matrix[1][2] * x3) / matrix[1][1]), 5)
    x1 = round(((matrix[0][3] - matrix[0][2] * x3 - matrix[0][1] * x2) / matrix[0][0]), 5)
    print("x =", x1, "y =", x2, "z =", x3)
solve([[1, -2, 3, 6], [2, -1, -1, 3], [3, -4, 1, 2
]])