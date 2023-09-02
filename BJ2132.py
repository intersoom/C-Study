testCase = input()
resultArr = []

for i in range(int(testCase)):
    resultArr = []
    N = input()
    for k in range(2, k*k<=N):
        while N % k == 0:
          resultArr.append(k)
          N /= k
    for j in set(resultArr):
      print(j, end=' ')
      print(resultArr.count(j))
