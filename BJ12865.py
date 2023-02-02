from sys import stdin

userInput = stdin.readline().split(' ')
N = int(userInput[0])
K = int(userInput[1])

WArr = [0]
VArr = [0]

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(N):
    WV = stdin.readline().split()
    WArr.append(int(WV[0]))
    VArr.append(int(WV[1]))
for i in range(1, N + 1):
    for j in range(K + 1):
        if WArr[i] <= j:
            dp[i][j] = max(dp[i - 1][j], VArr[i] + dp[i - 1][j - WArr[i]])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[N][K])