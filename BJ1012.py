import sys
from collections import deque

TC = int(sys.stdin.readline())

for _ in range(TC):
  count = 0
  que = deque([])

  MNK = sys.stdin.readline().split(' ')
  M = int(MNK[0])
  N = int(MNK[1])
  K = int(MNK[2])

  matrix = [[0 for __ in range(M)] for _ in range(N)]
  visited = [[0 for __ in range(M)] for _ in range(N)]

  for i in range(K):
    ind = sys.stdin.readline().split(' ')
    matrix[int(ind[1])][int(ind[0])] = 1

  for k in range(N):
    for q in range(M):
      if matrix[k][q] == 1 and visited[k][q] != 1:
        que.append([k, q])

        while que:
          current = que.pop()
          x = current[0]
          y = current[1]

          visited[x][y] = 1

          if x < N - 1:
            if matrix[x + 1][y] == 1 and visited[x + 1][y] != 1:
              que.append([x + 1, y])
              visited[x + 1][y] = 1
          if x > 0:
            if matrix[x - 1][y] == 1 and visited[x - 1][y] != 1:
              que.append([x - 1, y])
              visited[x - 1][y] = 1
          if y > 0:
            if matrix[x][y - 1] == 1 and visited[x][y - 1] != 1:
              que.append([x, y - 1])
              visited[x][y - 1] = 1
          if y < M - 1:
            if matrix[x][y + 1] == 1 and visited[x][y + 1] != 1:
              que.append([x, y + 1])
              visited[x][y + 1] = 1

        count += 1
  
  print(count)


