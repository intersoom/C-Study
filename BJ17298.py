import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' ')))

stack = deque(A[::-1])
maxStack = deque([])

for a in A[::-1]:
    if not maxStack:
        maxStack.append(a)
    else:
        top = maxStack[-1]

        if top >= a:
            maxStack.append(top)
        else:
            maxStack.append(a)

for a in A:
    while stack:
        poped = stack[-1]

        if a >= poped:
            stack.pop()
        else:
            print(poped, end=' ')
            break

    if not stack:
        print(-1)
