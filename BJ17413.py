import sys
from collections import deque

user = sys.stdin.readline()

words = user

tagMode = False
stacks = deque([])
stack = deque([])

for w in words:
  if w == '<':
    tagMode = True
    if stack:
      stacks.append(stack)
      stack = deque([])

  if tagMode:
    stack.appendleft(w)
  elif w != ' ' and w != '\n':
    stack.append(w)

  if w == '>':
    stacks.append(stack)
    stack = deque([])
    tagMode = False
  
  if not tagMode and w == ' ' or w == '\n':
    stack.appendleft(w)
    stacks.append(stack)
    stack = deque([])

for stack in stacks:
  while stack:
    print(stack.pop(), end='')