import sys
from collections import deque

MNH = list(map(int, sys.stdin.readline().split(' ')))
M = MNH[0]
N = MNH[1]
H = MNH[2]

matrix = []
visited = [[[False for _ in range(M)] for __ in range(N)] for ___ in range(H)]
q = deque([])

for h in range(H):
  temp = []
  for n in range(N):
    temp.append(list(map(int, sys.stdin.readline().split(' '))))
  matrix.append(temp)

isAllMature = True
# curDay = 0
day = 0
for h in range(H):
  for n in range(N):
    for m in range(M):
      if matrix[h][n][m] == 1 and not visited[h][n][m]:
        day = 0
        q.append([[h, n, m], day])
      elif isAllMature:
        isAllMature = False

while q:
  # print(q)
  poped = q.popleft()
  h_, n_, m_ = poped[0]
  day = poped[1]
  
  if h_ > 0:
    if not visited[h_-1][n_][m_] and matrix[h_-1][n_][m_] == 0:
      matrix[h_-1][n_][m_] = 1
      visited[h_-1][n_][m_] = True
      q.append([[h_-1, n_, m_], day+1])
  if h_ < H - 1:
    if not visited[h_+1][n_][m_] and matrix[h_+1][n_][m_] == 0:
      matrix[h_+1][n_][m_] = 1
      visited[h_+1][n_][m_] = True
      q.append([[h_+1, n_, m_], day+1])
  if n_ > 0:
    if not visited[h_][n_-1][m_] and matrix[h_][n_-1][m_] == 0:
      matrix[h_][n_-1][m_] = 1
      visited[h_][n_-1][m_] = True
      q.append([[h_, n_-1, m_], day+1])
  if n_ < N - 1:
    if not visited[h_][n_+1][m_] and matrix[h_][n_+1][m_] == 0:
      matrix[h_][n_+1][m_] = 1
      visited[h_][n_+1][m_] = True
      q.append([[h_, n_+1, m_], day+1])
  if m_ > 0:
    if not visited[h_][n_][m_-1] and matrix[h_][n_][m_-1] == 0:
      matrix[h_][n_][m_-1] = 1
      visited[h_][n_][m_-1] = True
      q.append([[h_, n_, m_-1], day+1])
  if m_ < M - 1:
    if not visited[h_][n_][m_+1] and matrix[h_][n_][m_+1] == 0:
      matrix[h_][n_][m_+1] = 1
      visited[h_][n_][m_+1] = True
      q.append([[h_, n_, m_+1], day+1])

BREAK = False
if isAllMature:
  print(0)
else:
  for h in range(H):
    if BREAK:
      break
    for n in range(N):
      if BREAK:
        break
      for m in range(M):
        if matrix[h][n][m] == 0:
          BREAK = True
          break
  if BREAK:
    print(-1)
  else:
    print(day)
          