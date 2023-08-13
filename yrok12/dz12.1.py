import random

#Создание матрицы
def randomMatrix(x, y):
    tmp = []
    for i in range(x):
        tmp.append([random.randrange(-500, 500, 1) for j in range(y)])
    return tmp

#Сложение двух матриц
def addingMatrix(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    result_matrix = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result_matrix

matrixSize = list(map(int, input("Введите размер матриц для сложения (2 числа через пробел): ").split()))

matrix1 = randomMatrix(matrixSize[0], matrixSize[1])
matrix2 = randomMatrix(matrixSize[0], matrixSize[1])

print(addingMatrix(matrix1, matrix2))
