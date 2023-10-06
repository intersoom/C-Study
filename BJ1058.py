import sys
import copy

N = int(sys.stdin.readline())

linkedList = [[] for _ in range(N)]
counts = []


for n in range(N):
  YN = sys.stdin.readline()
  for yn in range(N):
    if YN[yn] == 'Y':
      linkedList[n].append(yn)

linkedList2 = copy.deepcopy(linkedList)

for n in range(N):
  for x in linkedList[n]:
    for y in linkedList[x]:
      if y not in linkedList2[n] and y != n:
        linkedList2[n].append(y)
        
print(len(max(linkedList2, key=len)))