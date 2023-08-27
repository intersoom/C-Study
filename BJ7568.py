import sys
N = int(sys.stdin.readline())

arr = []
result = []
start = 0
end = 0


for i in range(N):
  temp = sys.stdin.readline().split(' ')
  temp[0] = int(temp[0])
  temp[1] = int(temp[1])

  arr.append(temp)

# 몸무게로 정렬
arr1 = sorted(arr, key=lambda x: (-x[0], -x[1]))
# 키로 정렬
arr2 = sorted(arr, key=lambda x: -x[1])

count = 1

# arr1[0].append(1)



print(arr1)
print(arr2)
 
# for i in arr:
#   count += 1
#   if count == N:
#     print(i[2])
#   else:
#     print(i[2], end=' ')
  