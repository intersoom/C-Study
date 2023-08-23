import sys
sys.setrecursionlimit(10**7)

userInput = int(input())

dp = [0] * (userInput + 1)

for i in range(2, userInput + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[userInput])

#### top-bottom으로는 못 푸나..

# def solve(x):
#     if x == 1:
#         return 0
    
#     if dp[x] != 0:
#         return dp[x]
    
#     dp[x] = solve(x - 1) + 1

#     if x % 2 == 0:
#         dp[x] = min(dp[x], solve(x // 2) + 1)
    
#     if x % 3 == 0:
#         dp[x] = min(dp[x], solve(x // 3) + 1)

#     return dp[x]

# print(solve(userInput))