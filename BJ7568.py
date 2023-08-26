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

arr1 = sorted(arr, key=lambda x: -x[0])
arr2 = sorted(arr, key=lambda x: -x[1])
print(arr)

for i in range(len(arr1)):
  if start == 0 and arr1[i] != arr2[i]:
    start = i
  elif arr1[i] != arr2[i]:
    end = i

for i in range(0, start):
  arr1[i].append(i + 1)
  result.append(arr1[i])

for i in range(start, end + 1):
  arr1[i].append(start + 1)
  result.append(arr1[i])

for i in range(end + 1, len(arr1)):
  arr1[i].append(i + 1)
  result.append(arr1[i])


for i in arr:
  for j in result:
    if i[0] == j[0] and i[1] == j[1]:
      if j == result[N - 1]:
        print(j[2])
      else:
        print(j[2], end=' ')
      
      break