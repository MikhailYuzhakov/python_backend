# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
import copy


def printmatrix(array):
    for i in range(len(array[0])):
        for j in range(len(array)):
            print(array[i][j], end=" ")
        print(end="\n")


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = copy.deepcopy(matrix)
print("Исходная матрица:")
printmatrix(matrix)
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        new_matrix[j][i] = matrix[i][j]

print("Транспорнированная матрица: ")
printmatrix(new_matrix)
