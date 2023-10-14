import sys
from collections import deque

user = sys.stdin.readline()
N = len(user)
M = int(sys.stdin.readline())

left = deque([])
right = deque([])

for i in user:
  if i != '\n':
    left.append(i)

for i in range(M):
  command = sys.stdin.readline()
  
  if command[0] == 'L':
    if left:
      poped = left.pop()
      right.appendleft(poped)
  elif command[0] == 'D':
    if right:
      poped = right.popleft()
      left.append(poped)
  elif command[0] == 'B':
    if left:
      left.pop()
  elif command[0] == 'P':
    left.append(command[2])
  
result = left + right

for i in result:
  print(i, end='')