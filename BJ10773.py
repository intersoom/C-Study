import sys
from collections import deque

K = int(sys.stdin.readline())
q = deque([])

for i in range(K):
  temp = int(sys.stdin.readline())

  if temp != 0:
    q.append(temp)
  else:
    q.pop()

print(sum(q))