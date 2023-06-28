n = int(input())
arr = []
dp = []
result = []
checkCon = [0] * n

for i in range(n):
    arr.append(int(input()))

for i in range(2, n):
    if i == 2:
        dp = [[arr[i - 2], arr[i - 1], 0], [arr[i - 2], 0, arr[i]], [0, arr[i - 1], arr[i]]]
    elif i == n - 1 or i == n - 2:
        for k in range(3):
            if dp[k][-1] == 0:
                dp[k].append(arr[i])
            elif dp[k][-2] == 0:
                dp[k].append(arr[i])
            else:
                dp[k].append(0)
    else:
        for k in range(3):
            if dp[k][-1] == 0:
                if dp[k][-2] == 0:
                    dp[k].append(arr[i])
                else:
                    if arr[i] + arr[i + 1] <= arr[i + 1] + arr[i + 2]:
                        dp[k].append(0)
                    else:
                        dp[k].append(arr[i])
            elif dp[k][-2] == 0:
                if arr[i] + arr[i + 1] <= arr[i + 1] + arr[i + 2]:
                    dp[k].append(0)
                else:
                    dp[k].append(arr[i])
            else:
                dp[k].append(0)
    print(dp)
for i in range(3):
    result.append(sum(dp[i]))

print(max(result))