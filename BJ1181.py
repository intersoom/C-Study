import sys

arr = []
N = int(sys.stdin.readline())

for i in range(N):
  userinput = sys.stdin.readline()
  arr.append(userinput)

arr = list(set(arr))
arr.sort(key=lambda x : (len(x), x))

for i in arr:
  print(i, end='')