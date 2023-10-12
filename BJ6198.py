import sys
from collections import deque
import copy

N = int(sys.stdin.readline())

buildings = deque([])
stack = deque([])
result = 0

for i in range(N):
  buildings.append(int(sys.stdin.readline()))

for b in buildings:
  while stack and b >= stack[-1]:
    stack.pop()
  result += len(stack)

  stack.append(b)

print(result)
  


