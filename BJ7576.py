from sys import stdin
from collections import deque

NM = stdin.readline().split(' ')
M = int(NM[0])
N = int(NM[1])

arr = []
tempArr = []

queue = deque([])
count = -1

# [x좌표, y좌표, count]
# x좌표가 세로 N, y좌표가 가로 M

# 2차원 배열 형성하면서 값에 1 있는 경우 큐에 넣기
for i in range(N):
    user = stdin.readline()
    tempArr = user.split(' ')
    for j in range(M):
        tempArr[j] = int(tempArr[j])
        if tempArr[j] == 1:
            queue.append([i, j, count])
    arr.append(tempArr)
    tempArr = []

while len(queue) > 0:
    x = queue[0][0]
    y = queue[0][1]
    count = queue[0][2]
    count += 1
    queue.popleft()

    # 좌우위아래 검사해서 0인 경우, 1로 바꾸고 큐에 넣기
    if x < N - 1 and arr[x + 1][y] == 0:
        queue.append([x + 1, y, count])
        arr[x + 1][y] = 1
    if x > 0 and arr[x - 1][y] == 0:
        queue.append([x - 1, y, count])
        arr[x - 1][y] = 1
    if y < M - 1 and arr[x][y + 1] == 0:
        queue.append([x, y + 1, count])
        arr[x][y + 1] = 1
    if y > 0 and arr[x][y - 1] == 0:
        queue.append([x, y - 1, count])
        arr[x][y - 1] = 1

noZero = 0

# 0 없는지 검사
for i in range(N):
    if 0 not in arr[i]:
        noZero += 1

# 0 없으면 count 출력
if noZero == N:
    print(count)
# 0 있으면 -1 출력
else:
    print(-1)

