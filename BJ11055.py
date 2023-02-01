from sys import stdin

# 점화식 : dp[n] = max(dp[n], dp[n - k] + x[n])

T = int(stdin.readline())
arr = stdin.readline().split(' ')

N = []
dp = []

for i in arr:
    N.append(int(i))
    # 후에 비교를 위해서 dp에도 똑같은 값을 넣어줍니다!
    dp.append(int(i))

for i in range(T):
    # j보다 작은 인덱스의 값들을 테스트
    for j in range(i):
        # 증가 하는 값인 경우, 기존에 dp에 들어가 있는 증가 하는 값과 비교 해서 크면 대체 시키기
        # dp[j]에다가 더해 줘야 하는 이유는 그 값은 증가 하는 값의 모임인 것이 이미 증명됨
        # 그냥 dp[j] + N[i]를 넣으면 안되는 경우 => max 사용하는 이유,
        # 2 11 3 14 1 200 100 5 101 13 -> 201
        # 앞에 더 큰 게 있었어도 그걸 판별 안 하고 덮어버리니까
        if N[i] > N[j]:
            dp[i] = max(dp[i], dp[j] + N[i])

print(max(dp))