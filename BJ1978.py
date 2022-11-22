userNum = input()
num_list = list(map(int, input().split()))
arr = []
arr_ = []
answer = 0


for i in range(0, max(num_list) + 1):
    arr.append(i)

for i in range(2, max(num_list) + 1):
    if arr[i] == 0:
        continue
    for j in range(i+i, max(num_list) + 1, i):
        arr[j] = 0

for i in range(2, max(num_list) + 1):
    if arr[i] != 0:
        arr_.append(arr[i])

for i in num_list:
    if i in arr_:
        answer += 1

print(answer)