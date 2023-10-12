import sys
from collections import deque

TC = int(sys.stdin.readline())

for tc in range(TC):
  convList = deque([])
  visited = deque([])
  convCount = int(sys.stdin.readline())

  home = list(map(int, sys.stdin.readline().split(' ')))

  for c in range(convCount):
    conv = list(map(int, sys.stdin.readline().split(' ')))
    convList.append(conv)
    visited.append(False)

  rock = list(map(int, sys.stdin.readline().split(' ')))

  result = 'sad'

  q = deque([])
  
  q.append(home)

  while q:
    poped = q.popleft()

    if abs(rock[0] - poped[0]) + abs(rock[1] - poped[1]) <= 1000:
      result = 'happy'
      break

    for i in range(convCount):
      if not visited[i]:
        if abs(convList[i][0] - poped[0]) + abs(convList[i][1] - poped[1]) <= 1000:
          visited[i] = True
          q.append(convList[i])
  if result != 'happy':
    result = 'sad'

  print(result)

  