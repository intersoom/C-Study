import sys
from collections import deque

N = int(sys.stdin.readline())
Ns = list(map(int, sys.stdin.readline().split(' ')))

stack = deque([[Ns[-1], N-1]])
result = [0] * N
poped = [0]

for current in range(N-2, -1, -1):
  n = Ns[current]

  while stack:
    poped = stack[-1]
    
    if poped[0] < n:
      stack.pop()
      result[poped[1]] = (current + 1)
    else:
      break

  stack.append([n, current])

for i in result:
  print(i, end=' ')