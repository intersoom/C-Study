import sys
from bisect import bisect_left, bisect_right 

result = []

N = sys.stdin.readline()
temp = sys.stdin.readline().split(' ')
NArr = []

for n in temp:
  NArr.append(int(n))

M = sys.stdin.readline()
temp = sys.stdin.readline().split(' ')
MArr = []

for m in temp:
  MArr.append(int(m))
  result.append(0)

NArr.sort()

count = 0


for target in MArr:
  result[count] = bisect_right(NArr, target) - bisect_left(NArr, target)
  count += 1

for i in result:
  print(i, end=' ')