from sys import stdin
from collections import deque

N = int(stdin.readline())

arr = []
tempArr = []
noneTempArr = []
noneArr = []

for i in range(N):
    user = input()
    for j in range(N):
        tempArr.append(user[j])
        noneTempArr.append(user[j])
    arr.append(tempArr)
    noneArr.append(noneTempArr)
    tempArr = []
    noneTempArr = []

queue = deque([])

colorWeak = 0
noneColorWeak = 0

# 적록색약 버전 구하기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R' or arr[i][j] == 'G':
            queue.append([i, j])
            while queue:
                x = queue[0][0]
                y = queue[0][1]

                pop = queue.popleft()

                if x < N - 1:
                    if arr[x + 1][y] == 'R' or arr[x + 1][y] == 'G':
                        queue.append([x + 1, y])
                        arr[x + 1][y] = 'K'
                if x > 0:
                    if arr[x - 1][y] == 'R' or arr[x - 1][y] == 'G':
                        queue.append([x - 1, y])
                        arr[x - 1][y] = 'K'
                if y < N - 1:
                    if arr[x][y + 1] == 'R' or arr[x][y + 1] == 'G':
                        queue.append([x, y + 1])
                        arr[x][y + 1] = 'K'
                if y > 0:
                    if arr[x][y - 1] == 'R' or arr[x][y - 1] == 'G':
                        queue.append([x, y - 1])
                        arr[x][y - 1] = 'K'
            colorWeak += 1
        elif arr[i][j] == 'B':
            queue.append([i, j])
            while queue:
                x = queue[0][0]
                y = queue[0][1]

                pop = queue.popleft()

                if x < N - 1:
                    if arr[x + 1][y] == 'B':
                        queue.append([x + 1, y])
                        arr[x + 1][y] = 'K'
                if x > 0:
                    if arr[x - 1][y] == 'B':
                        queue.append([x - 1, y])
                        arr[x - 1][y] = 'K'
                if y < N - 1:
                    if arr[x][y + 1] == 'B':
                        queue.append([x, y + 1])
                        arr[x][y + 1] = 'K'
                if y > 0:
                    if arr[x][y - 1] == 'B':
                        queue.append([x, y - 1])
                        arr[x][y - 1] = 'K'
            colorWeak += 1

# 안 색약
for i in range(N):
    for j in range(N):
        if noneArr[i][j] == 'R':
            queue.append([i, j])
            while queue:
                x = queue[0][0]
                y = queue[0][1]

                pop = queue.popleft()

                if x < N - 1:
                    if noneArr[x + 1][y] == 'R':
                        queue.append([x + 1, y])
                        noneArr[x + 1][y] = 'K'
                if x > 0:
                    if noneArr[x - 1][y] == 'R':
                        queue.append([x - 1, y])
                        noneArr[x - 1][y] = 'K'
                if y < N - 1:
                    if noneArr[x][y + 1] == 'R':
                        queue.append([x, y + 1])
                        noneArr[x][y + 1] = 'K'
                if y > 0:
                    if noneArr[x][y - 1] == 'R':
                        queue.append([x, y - 1])
                        noneArr[x][y - 1] = 'K'
            noneColorWeak += 1

        elif noneArr[i][j] == 'G':
            queue.append([i, j])
            while queue:
                x = queue[0][0]
                y = queue[0][1]

                pop = queue.popleft()

                if x < N - 1:
                    if noneArr[x + 1][y] == 'G':
                        queue.append([x + 1, y])
                        noneArr[x + 1][y] = 'K'
                if x > 0:
                    if noneArr[x - 1][y] == 'G':
                        queue.append([x - 1, y])
                        noneArr[x - 1][y] = 'K'
                if y < N - 1:
                    if noneArr[x][y + 1] == 'G':
                        queue.append([x, y + 1])
                        noneArr[x][y + 1] = 'K'
                if y > 0:
                    if noneArr[x][y - 1] == 'G':
                        queue.append([x, y - 1])
                        noneArr[x][y - 1] = 'K'
            noneColorWeak += 1
        elif noneArr[i][j] == 'B':
            queue.append([i, j])
            while queue:
                x = queue[0][0]
                y = queue[0][1]

                pop = queue.popleft()

                if x < N - 1:
                    if noneArr[x + 1][y] == 'B':
                        queue.append([x + 1, y])
                        noneArr[x + 1][y] = 'K'
                if x > 0:
                    if noneArr[x - 1][y] == 'B':
                        queue.append([x - 1, y])
                        noneArr[x - 1][y] = 'K'
                if y < N - 1:
                    if noneArr[x][y + 1] == 'B':
                        queue.append([x, y + 1])
                        noneArr[x][y + 1] = 'K'
                if y > 0:
                    if noneArr[x][y - 1] == 'B':
                        queue.append([x, y - 1])
                        noneArr[x][y - 1] = 'K'
            noneColorWeak += 1

print(noneColorWeak, colorWeak)