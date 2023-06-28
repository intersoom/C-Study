N = int(input())
NList = input()
NList = NList.split(' ')

arr = []
dp = []

for i in NList:
    arr.append(int(i))
    dp.append(1)

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))