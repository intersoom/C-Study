from sys import stdin

T = int(stdin.readline())
arr = stdin.readline().split(' ')

N = []
dp = []

for i in arr:
    N.append(int(i))
    dp.append(int(1))

for i in range(T):
    for j in range(i):
        if N[i] < N[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))