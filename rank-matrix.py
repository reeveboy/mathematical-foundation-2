# Rank of Matrix

import numpy as np
import sys
 
n = int(input('Enter number of unknowns: '))
matrix = np.zeros((n, n))
rank = 0

# Inputing Matrix
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
  for j in range(n):
    matrix[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Apply Gausian Elimination Algorithm 
for i in range(n):
  if matrix[i][i] == 0.0:
    break
        
  for j in range(i+1, n):
    ratio = matrix[j][i]/matrix[i][i]
      
    for k in range(n):
      matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    

for row in matrix:
  for val in row:
    if val != 0:
      rank += 1
      break

print(f"Rank of the matrix is: {rank}")

print(matrix)

# {{10,   20,   10},
# {20,   40,   20},
# {30,   50,   0}}

# {{10,   20,   10},
# {-20, -30,   10},
# {30,   50,   0}}