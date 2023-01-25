from sys import stdin
from collections import deque

user = stdin.readline()
userSplit = user.split(' ')

N = int(userSplit[0])
K = int(userSplit[1])

list = [0] * 100001

if K < N:
    print(N - K)
elif K > N:
    q = deque([])
    count = 0
    q.append([N, count])

    while list[K] != 1:
        index = q[0][0]
        count = q[0][1]
        q.popleft()

        if not list[index]:
            list[index] = 1

        count += 1

        if 0 <= index - 1 <= 100000:
            if not list[index - 1]:
                list[index - 1] = 1
                q.append([index - 1, count])
        if 0 <= index + 1 <= 100000:
            if not list[index + 1]:
                list[index + 1] = 1
                q.append([index + 1, count])
        if 0 <= index * 2 <= 100000:
            if not list[2 * index]:
                list[2 * index] = 1
                q.append([index * 2, count])
    print(count)
else:
    print(0)
