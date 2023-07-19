import sys

N = int(sys.stdin.readline())
NArr = sys.stdin.readline().split(' ')
M = int(sys.stdin.readline())
MArr = sys.stdin.readline().split(' ')

NArr = [int (i) for i in NArr]
MArr = [int (i) for i in MArr]

NArr.sort()

def binary_search(target, data):
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return 1
        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return 0

for i in MArr:
    print(binary_search(i, NArr))