import sys
N = int(sys.stdin.readline())

arr = []

for i in range(N):
  temp = sys.stdin.readline().split(' ')
  temp[0] = int(temp[0])
  temp[1] = int(temp[1])

  arr.append(temp)

for i in range(N):
  rank = 1
  for j in range(N):
    if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
      rank += 1
  print(rank, end=' ')