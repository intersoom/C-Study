import sys
sys.setrecursionlimit(10**6)

NM = sys.stdin.readline().split(' ')
N = int(NM[0])
M = int(NM[1])
res = 0

graph = [[] for i in range(1001)]
visited = [0 for i in range(1001)]

def dfs(cur):
  visited[cur] = 1
  for i in graph[cur]:
    if not visited[i]:
      dfs(i)

for i in range(M):
  uv = sys.stdin.readline().split(' ')
  u = int(uv[0])
  v = int(uv[1])
  graph[u].append(v)
  graph[v].append(u)

for i in range(1, N+1):
  if visited[i]: continue
  res += 1
  dfs(i)

print(res)