# Reduced Echelon Form 

import numpy as np
import sys
 
n = int(input('Enter number of unknowns: '))
matrix = np.zeros((n,n+1))
solutions = np.zeros(n)

# Inputing Matrix
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        matrix[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Apply Gausian Elimination Algorithm to all values of i and j expect when i == j
for i in range(n):
    if matrix[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
         
    for j in range(n):
        if i == j:
            continue
        ratio = matrix[j][i]/matrix[i][i]
         
        for k in range(n+1):
            matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

# Converting the diagonal values to 1
for i in range(n):
    matrix[i] = matrix[i] / matrix[i][i]
 
# Solving and storing last unknown
solutions[n-1] = matrix[n-1][n]/matrix[n-1][n-1]
 
# Back Substituting and solving other unknowns
for i in range(n-2,-1,-1):
    solutions[i] = matrix[i][n]
     
    for j in range(i+1,n):
        solutions[i] = solutions[i] - matrix[i][j]*solutions[j]
     
    solutions[i] = solutions[i]/matrix[i][i]
 
# Printing solutions
print('\nThe solution is: ')
for i in range(n):
    print(f'X{i+1} = {solutions[i]}', end = '\t')

print()
print()

print(matrix)
