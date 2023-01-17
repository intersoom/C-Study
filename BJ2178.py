NM = input().split(' ')
N = int(NM[0])
M = int(NM[1])

arr = []

used = []
tempArr = []

for i in range(N):
    user = input()
    for j in range(M):
        tempArr.append(int(user[j]))
    arr.append(tempArr)
    tempArr = []

# [x좌표, y좌표, count]
# x좌표가 세로 N, y좌표가 가로 M
queue = [[0, 0, 1]]
count = 1

while queue[0][0] != N - 1 or queue[0][1] != M - 1:
    x = queue[0][0]
    y = queue[0][1]
    count = queue[0][2]
    # print(queue)
    pop = queue.pop(0)
    # print(pop)


    count += 1

    # 확인 조건: index가 0과 N - 1 또는 M - 1 사이인지
    # value가 1인 경우, 넣기! -1이면 넣지 않기!
    if x < N - 1:
        if arr[x + 1][y] == 1:
            queue.append([x + 1, y, count])
            arr[x + 1][y] = -1
    if x > 0:
        if arr[x - 1][y] == 1:
            queue.append([x - 1, y, count])
            arr[x - 1][y] = -1
    if y < M - 1:
        if arr[x][y + 1] == 1:
            queue.append([x, y + 1, count])
            arr[x][y + 1] = -1
    if y > 0:
        if arr[x][y - 1] == 1:
            queue.append([x, y - 1, count])
            arr[x][y - 1] = -1
    if [N - 1, M - 1, count] in queue:
        print(count)
        break

# print(count)