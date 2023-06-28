from sys import stdin
from collections import deque

user = stdin.readline()
userSplit = user.split(' ')

F = int(userSplit[0])
S = int(userSplit[1])
G = int(userSplit[2])
U = int(userSplit[3])
D = int(userSplit[4])

list = [0] * (F + 1)

if S == G:
    print(0)
else:
    q = deque([])
    count = 0
    q.append([S, count])

    while q:
        index = q[0][0]
        count = q[0][1]

        q.popleft()

        if not list[index]:
            list[index] = 1

        count += 1

        if 1 <= index + U <= F:
            if not list[index + U]:
                list[index + U] = 1
                q.append([index + U, count])
                if list[G] == 1:
                    break
        if 1 <= index - D <= F:
            if not list[index - D]:
                list[index - D] = 1
                q.append([index - D, count])
                if list[G] == 1:
                    break

    if list[G] == 1:
        print(count)
    else:
        print('use the stairs')
