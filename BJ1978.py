userNum = input()
# input 값을 split해서 리스트의 형태로 만든다
num_list = list(map(int, input().split()))

arr = []
arr_ = []
answer = 0

# 0 ~ 입력 받은 리스트에서 가장 큰 수까지 수를 arr에 담아줌
for i in range(0, max(num_list) + 1):
    arr.append(i)

for i in range(2, max(num_list) + 1):
    # 이미 0 들어간 것들은 건너뛰기
    if arr[i] == 0:
        continue
    # i씩 더해서 배수들의 값에 0 넣기
    for j in range(i+i, max(num_list) + 1, i):
        arr[j] = 0

for i in range(2, max(num_list) + 1):
    # 0이 들어가지 않은 수들이 소수이기 때문에 arr_ 리스트에 추가해줌
    if arr[i] != 0:
        arr_.append(arr[i])

# arr_ 개수가 소수의 개수이기 때문에 +1씩 해줘서 정답을 구해줌!
for i in num_list:
    if i in arr_:
        answer += 1

print(answer)