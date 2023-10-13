import sys
from collections import deque

targets = deque([])

stack = deque([])
result = deque([])
no = False

N = int(sys.stdin.readline())

top = 1

for i in range(N):
  target = int(sys.stdin.readline())

  
  while True:
    if top <= target: 
      for i in range(top, target + 1):
        stack.append(i)
        result.append('+')
      top = target + 1
    elif stack:
      poped = stack.pop()
      result.append('-')
      if poped == target:
        break
    else:
      no = True
      break

if no:
  print('NO')
else:
  for i in result:
    print(i)