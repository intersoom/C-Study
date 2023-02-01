from sys import stdin

T = int(stdin.readline())
result = [[],[]]
N = []
size = 0

answer = 0

for _ in range(T):
    N = []
    stickers = []
    size = int(stdin.readline())
    result = [[0] * size, [0] * size]

    first = stdin.readline().split(' ')
    second = stdin.readline().split(' ')

    tempArr = []

    for i in first:
        tempArr.append(int(i))
    N.append(tempArr)

    tempArr = []
    for i in second:
        tempArr.append(int(i))
    N.append(tempArr)

    for n in range(size):
        if size == 1:
            answer = max(N[0][0], N[1][0])
            break
        elif size == 2:
            if N[0][0] + N[1][1] > N[0][1] + N[1][0]:
                answer = N[0][0] + N[1][1]
                break
            else:
                answer = N[0][1] + N[1][0]
                break

        if n == 0:
            result[0][0] = N[0][0]
            result[1][0] = N[1][0]

        elif n == 1:
            result[1][1] = result[0][0] + N[1][1]
            result[0][1] = result[1][0] + N[0][1]
        # last
        elif n == size - 1:
            if result[1][n - 1] > result[1][n - 2]:
                result[0][n] = result[1][n - 1] + N[0][n]
            else:
                result[0][n] = result[1][n - 2] + N[0][n]

            if result[0][n - 1] > result[0][n - 2]:
                result[1][n] = result[0][n - 1] + N[1][n]
            else:
                result[1][n] = result[0][n - 2] + N[1][n]

            if result[1][n] > result[0][n]:
                answer = result[1][n]
            else:
                answer = result[0][n]
        # 3부터!
        else:
            if result[1][n - 1] > result[1][n - 2]:
                result[0][n] = result[1][n - 1] + N[0][n]
            else:
                result[0][n] = result[1][n - 2] + N[0][n]

            if result[0][n - 1] > result[0][n - 2]:
                result[1][n] = result[0][n - 1] + N[1][n]
            else:
                result[1][n] = result[0][n - 2] + N[1][n]

    print(answer)