# N, M의 값을 split 메소드를 이용해서 구해준다
size = input()
N = int(size.split(' ')[0])
M = int(size.split(' ')[1])

# 빈 리스트를 생성해준다
arr = []

# N번 입력받고 한 줄에 있는 숫자를 문자열의 특징을 활용하여 인덱스로 접근해서 int형으로 변환해서
# tempArr에 넣어주고 해당 리스트를 arr에 넣어서 2차원 배열을 생성해준다
for i in range(N):
    temp = input()
    tempArr = []
    for j in range(M):
        tempArr.append(int(temp[j]))
    arr.append(tempArr)

# k는 j에서부터의 거리를 구하는 아이
# length는 j부터 k까지의 거리
# max에는 정사각형의 최소 크기는 1이기 때문에 1을 초기값으로 설정해준다
k = 0
length = 0
max = 1

# arr의 첫번째 인덱스에 있는 리스트부터 N번째 인덱스에 있는 리스트까지 돌린다
for i in range(N):
    # j를 기준으로 k를 한 칸씩 움직이며 j의 인덱스에 있는 숫자와 k의 인덱스에 있는 숫자가 같은지 다른지 비교

    for j in range(M):
        k = j + 1
        while k < M:
            # 1) j의 인덱스에 있는 숫자 === k의 인덱스에 있는 숫자인 경우,
            if arr[i][j] == arr[i][k]:
                # 먼저 사이의 길이를 구해준다
                length = k - j
                # N의 길이보다 i에 length를 더한 값이 작은지 확인하여 비교할 값의 존재 여부 확인
                if i + length < N:
                    # j의 위치에서 length만큼 i에 더한 값과 비교
                    if arr[i+length][j] == arr[i][j]:
                        # k의 위치에서 length만큼 i에 더한 값과 비교
                        if arr[i + length][k] == arr[i][k]:
                            # max에 들어있는 값과 현재 구한 정사각형 크기와 비교해서 더 크면 값을 대체하여 넣어줌
                            # (정사각형 크기를 구하는 것은 +1 해줌, 기존의 length 값은 사이의 크기)
                            if max < (length + 1) * (length + 1):
                                max = (length + 1) * (length + 1)
                            # k+1 해서 다시 비교해줌
                            k += 1
                        else:
                            k += 1
                    else:
                        k += 1
                else:
                    k += 1
            else:
                k += 1
print(max)