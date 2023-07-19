import sys
import heapq

heap = []
negativeCheck = {}

N = int(sys.stdin.readline())

for i in range(N):
  userInput = int(sys.stdin.readline())
  if userInput == 0:
    if len(heap) == 0:
      print(0)
      continue
    else:
      poped = heapq.heappop(heap)
      if poped in negativeCheck and negativeCheck[poped] > 0:
        negativeCheck[poped] -= 1
        print(-poped)
      else:
        print(poped)
  else:
    heapq.heappush(heap, abs(userInput))

    if userInput < 0:
      if abs(userInput) in negativeCheck:
        negativeCheck[abs(userInput)] += 1
      else:
        negativeCheck[abs(userInput)] = 1