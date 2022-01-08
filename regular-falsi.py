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

a = np.zeros(2)
b = np.zeros(2)
xr = np.zeros(2)

a[0] = float(input("Enter initial guess a: "))
b[0] = float(input("Enter initial guess b: "))

a[1] = executeFunc(a[0])
b[1] = executeFunc(b[0])

iteration = 0
xrs = []
error = 100

while True:
  a[0] = float(input("Enter initial guess xl: "))
  b[0] = float(input("Enter initial guess xu: "))

  a[1] = executeFunc(a[0])
  b[1] = executeFunc(b[0])

  if a[1] * b[1] < 0: # Points are valid
    break

  else:
    print("a and b are invalid. Pick new points")


while True:

  xr[0] = ((a[0] * b[1]) - (b[0] * a[1])) / (b[1] - a[1])
  xr[1] = executeFunc(xr[0])
  xrs.append(xr[0])

  temp = a[1] * xr[1]

  if iteration > 0:
    error = (xrs[iteration] - xrs[iteration-1]) / xrs[iteration]

  if temp < 0:
    b = xr
  elif temp > 0:
    a = xr
  else:
    print(f"The root is: {xr[0]}")
    break

  if error < errorPercent:
    print(f"Ea = {error} is less than {errorPercent}")
    print(f"Root is {xr[0]}")
    break

  iteration += 1
