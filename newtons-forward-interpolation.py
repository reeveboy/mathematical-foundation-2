
def calcDiffRow(prev_col):
  col = []

  for i in range(1, len(prev_col)):
    col.append(prev_col[i] - prev_col[i-1])

  return col

def calcP(index):
  ans = p

  for i in range(1, index):
    ans *= p - i
  
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
p = (value - x[0]) / h

sum = y[0][0]
for i in range(1, n):
  sum += (y[i][0] * calcP(i)) / fact(i)

print(f"Interpolation value of {value} is {sum}")