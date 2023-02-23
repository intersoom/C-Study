testcase = ''
from collections import deque

while True:
    testcase = input()
    if testcase == '0 0':
        break

    w = int(testcase.split(' ')[0])
    h = int(testcase.split(' ')[1])
    arr = []
    visit = []
    tempArr = []
    tempVisit = []
    q = deque([])
    # q = []
    count = 0
    x = 0
    y = 0

    for i in range(h):
        temp = input().split(' ')
        for j in range(w):
            tempArr.append(int(temp[j]))
            tempVisit.append(0)
        arr.append(tempArr)
        visit.append(tempVisit)
        tempArr = []
        tempVisit = []

    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and arr[i][j] == 1:
                q.append([i, j])
                visit[i][j] = 1
                count += 1
                while q:
                    x = q[0][0]
                    y = q[0][1]
                    q.popleft()

                    if x < h - 1:
                        if visit[x + 1][y] == 0 and arr[x + 1][y] == 1:
                            q.append([x + 1, y])
                            visit[x + 1][y] = 1
                    if x > 0:
                        if visit[x - 1][y] == 0 and arr[x - 1][y] == 1:
                            q.append([x - 1, y])
                            visit[x - 1][y] = 1
                    if y < w - 1:
                        if visit[x][y + 1] == 0 and arr[x][y + 1] == 1:
                            q.append([x, y + 1])
                            visit[x][y + 1] = 1
                    if y > 0:
                        if visit[x][y - 1] == 0 and arr[x][y - 1] == 1:
                            q.append([x, y - 1])
                            visit[x][y - 1] = 1
                    if x < h - 1 and y < w - 1:
                        if visit[x + 1][y + 1] == 0 and arr[x + 1][y + 1] == 1:
                            q.append([x + 1, y + 1])
                            visit[x + 1][y + 1] = 1
                    if x < h - 1 and y > 0:
                        if visit[x + 1][y - 1] == 0 and arr[x + 1][y - 1] == 1:
                            q.append([x + 1, y - 1])
                            visit[x + 1][y - 1] = 1
                    if x > 0 and y < w - 1:
                        if visit[x - 1][y + 1] == 0 and arr[x - 1][y + 1] == 1:
                            q.append([x - 1, y + 1])
                            visit[x - 1][y + 1] = 1
                    if x > 0 and y > 0:
                        if visit[x - 1][y - 1] == 0 and arr[x - 1][y - 1] == 1:
                            q.append([x - 1, y - 1])
                            visit[x - 1][y - 1] = 1
                # print(count)

    print(count)