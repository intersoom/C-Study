import sys

arr = []

for i in range(9):
  arr.append(int(sys.stdin.readline()))

total = sum(arr)
over = total - 100
a, b = 0, 0

for i in arr:
  for j in arr:
    if i + j == over:
      a = i
      b = j

for i in arr:
  if i != a and i !=b:
    print(i)