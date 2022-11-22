testcase = int(input())
arr = [0] * 101
arr[1] = 1
arr[2] = 1
arr[3] = 1
result = []

for i in range(testcase):
    x = int(input())
    for k in range(4, x + 1):
        arr[k] = arr[k - 2] + arr[k - 3]
    result.append(arr[x])

for i in result:
    print(i)
