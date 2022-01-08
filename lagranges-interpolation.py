import numpy as np

n = int(input("Enter n: "))
matrix = np.zeros((n, 2))

print("Enter the set of data points: ")
for i in range(n):
  matrix[i][0] = float(input(f"Enter x{i}: "))
  matrix[i][1] = float(input(f"Enter f(x{i}): "))

x = float(input("Enter the value of x: "))

soln = 0
for i in range(n):
  numerator = 1
  for j in range(n):
    if j == i:
      continue
    if numerator == 0:
      break
    numerator *= (x - matrix[j][0])
    
  denominator = 1
  for j in range(n):
    if j == i:
      continue
    denominator *= (matrix[i][0] - matrix[j][0])

  soln += numerator / denominator * matrix[i][1]

print(f"The interpolating value of f({x}) is {soln}")
