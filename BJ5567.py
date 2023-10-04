import sys

invited = []

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

matrix = [[] for _ in range(N + 1)]

for i in range(M):
  ab = sys.stdin.readline().split(' ')
  a = int(ab[0])
  b = int(ab[1])

  matrix[a].append(b)
  matrix[b].append(a)

for a1 in matrix[1]:
  if a1 not in invited:
    invited.append(a1)
  for b1 in matrix[a1]:
    if b1 not in invited and b1 != 1:
      invited.append(b1)

print(len(invited))
