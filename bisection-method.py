import numpy as np

def executeFunc(x):
  soln = 0
  for i in range(n):
    if i == 0:
      soln += eqnList[i]
    else:
      soln += (x ** i) * eqnList[i]
      
  return soln

n = int(input("Enter n:"))

eqnList = np.ones((n))
for i in range(n-1, -1, -1):
  eqnList[i] = float(input(f"Enter coeffecient of x^{i}: "))

errorPercent = float(input("Enter the percent relative error: "))

xl = np.zeros(2)
xu = np.zeros(2)
xr = np.zeros(2)

while True:
  xl[0] = float(input("Enter initial guess xl: "))
  xu[0] = float(input("Enter initial guess xu: "))

  xl[1] = executeFunc(xl[0])
  xu[1] = executeFunc(xu[0])

  if xl[1] * xu[1] < 0: # Points are valid
    break

  else:
    print("xl and xu are invalid. Pick new points")

iteration = 0
xrs = [xr[0]]
error = 100

while True:

  xr[0] = (xl[0] + xu[0]) / 2
  xr[1] = executeFunc(xr[0])
  xrs.append(xr[0])

  temp = xl[1] * xr[1]

  if iteration > 1:
    error = (xrs[iteration] - xrs[iteration-1]) / xrs[iteration]

  if temp < 0:
    xu = xr
  elif temp > 0:
    xl = xr
  else:
    print(f"The root is: {xr[0]}")
    break

  if error < errorPercent:
    print(f"Ea = {error} is less than {errorPercent}")
    print(f"Root is {xr[0]}")
    break

  iteration += 1
