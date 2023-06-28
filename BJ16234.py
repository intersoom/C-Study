from sys import stdin
from collections import deque

NLR = stdin.readline()
NLR = NLR.split(' ')

N = int(NLR[0])
L = int(NLR[1])
R = int(NLR[2])

arr = []
visited = []
tempArr = []
tempVisit = []


for i in range(N):
    user = input().split(' ')
    for j in range(N):
        tempArr.append(int(user[j]))
        tempVisit.append(0)
    arr.append(tempArr)
    visited.append(tempVisit)
    tempArr = []
    tempVisit = []

q = deque([])
count = 0
answer = 0

turn = True
breaker = False
unite = []
uniteIndex = []

i = 0
j = 0

while turn:
    print(arr)
    while i < N:
        if breaker:
            breaker = False
            break
        i += 1
        while j < N:
            if visited[i][j] == 0:
                q.append([i, j, arr[i][j]])
                visited[i][j] = 1

                while q:
                    x = q[0][0]
                    y = q[0][1]
                    val = q[0][2]
                    pop = q.popleft()
                    uniteIndex.append(pop)
                    unite.append(val)

                    if x < N - 1:
                        if L <= abs(val - arr[x + 1][y]) <= R and visited[x + 1][y] == 0:
                            q.append([x + 1, y, arr[x + 1][y]])
                            visited[x + 1][y] = 1
                    if x > 0:
                        if L <= abs(val - arr[x - 1][y]) <= R and visited[x - 1][y] == 0:
                            q.append([x - 1, y, arr[x - 1][y]])
                            visited[x - 1][y] = 1
                    if y < N - 1:
                        if L <= abs(val - arr[x][y + 1]) <= R and visited[x][y + 1] == 0:
                            q.append([x, y + 1, arr[x][y + 1]])
                            visited[x][y + 1] = 1
                    if y > 0:
                        if L <= abs(val - arr[x][y - 1]) <= R and visited[x][y - 1] == 0:
                            q.append([x, y - 1, arr[x][y - 1]])
                            visited[x][y - 1] = 1
                if len(unite) > 1:
                    answer += 1
                    population = sum(unite) / len(unite)

                    for k in uniteIndex:
                        x = k[0]
                        y = k[1]

                        arr[x][y] = int(population)
                        visited[x][y] = 0
                    # # 초기화
                    i = 0
                    j = 0
                    unite = []
                    uniteIndex = []
                    breaker = True
                    break
                else:
                    breaker = True
                    turn = False
                    break
            j += 1


print(answer)