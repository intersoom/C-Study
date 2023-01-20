from sys import stdin
from collections import deque

N = int(input())

arr = []
tempArr = []

for i in range(N):
    user = input()
    for j in range(N):
        tempArr.append(int(user[j]))
    arr.append(tempArr)
    tempArr = []

queue = deque([])
count = 0
countArr = []
visited = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            queue.append([i, j])
            visited.append([i, j])
            count = 1

            while len(queue) > 0:
                x = queue[0][0]
                y = queue[0][1]
                pop = queue.popleft()

                if x < N - 1:
                    if arr[x + 1][y] == 1 and [x + 1, y] not in visited:
                        queue.append([x + 1, y])
                        visited.append([x + 1, y])
                        arr[x + 1][y] = 0
                        count += 1
                if x > 0:
                    if arr[x - 1][y] == 1 and [x - 1, y] not in visited:
                        queue.append([x - 1, y])
                        visited.append([x - 1, y])
                        arr[x - 1][y] = 0
                        count += 1
                if y < N - 1:
                    if arr[x][y + 1] == 1 and [x, y + 1] not in visited:
                        queue.append([x, y + 1])
                        visited.append([x, y + 1])
                        arr[x][y + 1] = 0
                        count += 1
                if y > 0:
                    if arr[x][y - 1] == 1 and [x, y - 1] not in visited:
                        queue.append([x, y - 1])
                        visited.append([x, y - 1])
                        arr[x][y - 1] = 0
                        count += 1
            countArr.append(count)

print(len(countArr))

countArr.sort()

for i in countArr:
    print(i)

