import sys
from collections import deque

input = ''

while True:
  stack = deque([])
  result = 'yes'

  input = sys.stdin.readline()

  if input[0] == '.':
    break
  else:
    for i in input:
      if i == '(' or i == '[':
        stack.append(i)
      elif i == ']':
        if stack:
          poped = stack.pop()

          if poped == '[':
            result = 'yes'
          else:
            result = 'no'
            break
        else:
          result = 'no'
          break
      elif i == ')':
        if stack:
          poped = stack.pop()

          if poped == '(':
            result = 'yes'
          else:
            result = 'no'
            break
        else:
          result = 'no'
          break
    
    if stack:
      result = 'no'
      
    print(result)