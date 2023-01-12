# # 인접행렬 방식 사용
computerNum = int(input())
linkNum = int(input())

arr = []
queue = [1]
used = []
tempArr = []

for i in range(computerNum + 1):
    arr.append(tempArr)
    tempArr = []
    for j in range(computerNum + 1):
        tempArr.append(0)

ab = []

for i in range(linkNum):
    ab = input().split(" ")
    a = int(ab[0])
    b = int(ab[1])

    arr[a][b] = 1
    arr[b][a] = 1

while len(queue) > 0:
    index = queue[0]
    pop = queue.pop(0)
    if pop not in used:
        used.append(pop)
    for i in range(1, computerNum + 1):
        if arr[index][i] == 1:
            if i not in used:
                queue.append(i)

print(len(used) - 1)

###############################################################
# 인접리스트 방식 사용
computerNum = int(input())
linkNum = int(input())

arr = []
queue = [1]
used = []
tempArr = []

for i in range(computerNum + 1):
    arr.append([])

ab = []

for i in range(linkNum):
    ab = input().split(" ")
    a = int(ab[0])
    b = int(ab[1])

    arr[a].append(b)
    arr[b].append(a)

while len(queue) > 0:
    index = queue[0]
    pop = queue.pop(0)
    if pop not in used:
        used.append(pop)

    for i in arr[index]:
        if i not in used:
            queue.append(i)

print(len(used) - 1)