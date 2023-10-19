import sys
from collections import deque

NK = list(map(int, sys.stdin.readline().split(' ')))
N = NK[0]
K = NK[1]

visited = [0] * 100001

result = 0
cnt = 0

maxTime = 100000

q = deque([N])

while q:
  poped = q.popleft()

  if poped == K:
    result = visited[poped]
    cnt += 1
    continue

  for i in [poped-1, poped+1, poped*2]:
    if 0<= i <= 100000 and (visited[i] == 0 or visited[i] == visited[poped] + 1):
      visited[i] = visited[poped] + 1
      q.append(i)
  
print(result)
print(cnt)