
def calcDiffRow(prev_col):
  col = []

  for i in range(1, len(prev_col)):
    col.append(prev_col[i] - prev_col[i-1])

  return col

def calcP(index):
  ans = p

  for i in range(1, index):
    ans *= p + i
  
  return ans

def fact(n):
  ans = 1

  for i in range(1, n+1):
    ans *= i

  return ans


n = int(input("Enter n:"))
x = []
y = []

diff_row = []
for i in range(n):
  x.append(float(input(f"Enter value of x{i}: ")))
  diff_row.append(float(input(f"Enter value of y{i}: ")))

y.append(diff_row)

count = 0
while True:
  if len(y[count]) < 2:
    break
  y.append(calcDiffRow(y[count]))
  count += 1


value = float(input("Enter the value to interpolate at: "))
h = x[1] - x[0]
p = (value - x[n-1]) / h

sum = y[0][n-1]
for i, j in enumerate(range(n-2, -1, -1)):
  sum += (y[i+1][j] * calcP(i+1)) / fact(i+1)

print(f"Interpolation value of {value} is {sum}")