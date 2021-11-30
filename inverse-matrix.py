import numpy as np
import sys
 
n = int(input('Enter number of unknowns: '))
matrix = np.zeros((n,n))
i_matrix = np.zeros((n,n))

# Inputing Matrix
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
  for j in range(n):
    matrix[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

    if i == j:
      i_matrix[i][j] = 1

# Apply Gausian Elimination Algorithm to all values of i and j expect when i == j
for i in range(n):

  if matrix[i][i] == 0:
    #s waping rows if a[i][i] == 0
    for k in range(i+1, n):
      if matrix[k][i] != 0:
        matrix[i] += matrix[k]
        matrix[k] -= matrix[i]
        matrix[i] -= matrix[k]
        break

  # to make a[i][i] = 1
  divisor = matrix[i][i]
  matrix[i] = matrix[i] / divisor
  i_matrix[i] = i_matrix[i] / divisor

  # row reduced form
  for j in range (n):
    if i == j:
      continue
    
    multiplier = matrix[j][i]
    
    matrix[j] -= matrix[i] * multiplier
    i_matrix[j] -= i_matrix[i] * multiplier
  

print(i_matrix)

