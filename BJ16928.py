import sys
from collections import deque

matrix = [0] * 101
visited = [False] * 101

q = deque([[2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]])

visited[2] = True
visited[3] = True
visited[4] = True
visited[5] = True
visited[6] = True
visited[7] = True

NM = list(map(int, sys.stdin.readline().split(' ')))
N = NM[0]
M = NM[1]

for i in range(N):
  ladder = list(map(int, sys.stdin.readline().split(' ')))
  matrix[ladder[0]] = ladder[1]

for i in range(M):
  snake = list(map(int, sys.stdin.readline().split(' ')))
  matrix[snake[0]] = snake[1]

dice = [1, 2, 3, 4, 5, 6]
wBreak = False

while q and not wBreak:
  poped = q.popleft()
  popedLoc = poped[0]
  popedCount = poped[1]
  
  if matrix[popedLoc] != 0:
    popedLoc = matrix[popedLoc]
  
  for d in dice:
    if not visited[popedLoc + d]:
      if popedLoc + d < 100:
        q.append([popedLoc + d, popedCount + 1])
        visited[popedLoc + d] = True
      elif popedLoc + d == 100:
        popedCount += 1
        wBreak = True
        break
    

print(popedCount)