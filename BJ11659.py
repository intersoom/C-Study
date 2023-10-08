import sys

NM = sys.stdin.readline().split(' ')
N = int(NM[0])
M = int(NM[1])

temp = sys.stdin.readline().split(' ')
arr = []
accumulation = [0]

for i in temp:
  arr.append(int(i))

sum = 0
for i in arr:
  sum += i
  accumulation.append(sum)

for i in range(M):
  ij = sys.stdin.readline().split(' ')
  i = int(ij[0])
  j = int(ij[1])
  print(accumulation[j] - accumulation[i-1])


