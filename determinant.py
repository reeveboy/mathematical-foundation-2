import numpy as np

def main():
    n = int(input('Enter n: '))
    matrix = np.zeros((n, n))

    # Inputing Matrix
    print('Enter the Matrix:')
    for i in range(n):
        for j in range(n):
            matrix[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

    print(determinant(matrix))


def determinant(matrix):
    if len(matrix) > 2:
        sol = 0
        for i in range(len(matrix)):
            new_matrix = np.delete(matrix, 0, 0)
            new_matrix = np.delete(new_matrix, i, 1)
            if i % 2 == 0:
                sol += matrix[0][i] * determinant(new_matrix)
            else:
                sol -= matrix[0][i] * determinant(new_matrix)
        return sol

    else:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])


main()