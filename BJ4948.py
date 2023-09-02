import sys

n = 1

arr = [1 for i in range(246913)]

for i in range(2, 246913):
  arr[i] = i

for i in range(2, 246913):
  if arr[i] == 0:
    continue
  for j in range(i + i, 246913, i):
    arr[j] = 0

while True:
  n = int(sys.stdin.readline())

  if n == 0:
    break

  count = 0

  for i in range(n + 1, 2 * n + 1):
    if arr[i] != 0:
      count += 1
  
  print(count)