N = int(input())
dp = [0] * N
dpSum = 0

for i in range(N):
    if i == 0:
        dp[0] = 10
    elif i == 1:
        for k in range(1, 11):
            dpSum += k
        dp[1] = dpSum
    else:
        temp = 0
        dpSum = dp[i - 1]
        for k in range(10):
            temp += (dp[i - 2] - k)
            dpSum += (dp[i - 1] - temp)
        dp[i] = dpSum
print(dp[N - 1] % 10007)