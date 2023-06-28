from sys import stdin

T = int(stdin.readline())

N = []
result = [[0, 0, 0] for _ in range(T)]

for i in range(T):
    arraySplit = stdin.readline().split(' ')
    tempArr = []
    for j in arraySplit:
        tempArr.append(int(j))
    N.append(tempArr)

for n in range(T):
    if n == 0:
        result[0][0] = N[0][0]
        result[0][1] = N[0][1]
        result[0][2] = N[0][2]
    else:
        result[n][0] = min(result[n - 1][1], result[n - 1][2]) + N[n][0]
        result[n][1] = min(result[n - 1][0], result[n - 1][2]) + N[n][1]
        result[n][2] = min(result[n - 1][1], result[n - 1][0]) + N[n][2]

    if n == T - 1:
        print(min(result[n][0], result[n][1], result[n][2]))