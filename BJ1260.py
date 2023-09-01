from collections import deque

NMV = input().split(' ')

graph = [[] for _ in range(1001)]
visited = [0 for _ in range(1001)]
visited2 = [0 for _ in range(1001)]

N = int(NMV[0])
M = int(NMV[1])
V = int(NMV[2])

for i in range(M):
  edge = input().split(' ')
  a = int(edge[0])
  b = int(edge[1])

  graph[a].append(b)
  graph[b].append(a)

for i in graph:
  i.sort()

## DFS
def dfs(cur):
  visited[cur] = 1
  print(cur, end=' ')
  for i in graph[cur]:
    if not visited[i]:
      dfs(i)

dfs(V)

print()
# BFS
q = deque()

q.append(V)

while len(q) > 0:
  a = q.popleft()
  if not visited2[a]:
    print(a, end=' ')
  
  visited2[a] = 1

  for i in graph[a]:
    if not visited2[i]:
      q.append(i)