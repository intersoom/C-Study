import heapq
import sys

heap = []
curArr = []


N = int(sys.stdin.readline())

for i in range(N):
    # curArr.append(int(sys.stdin.readline()))
    cur = int(sys.stdin.readline())
              
    if cur == 0:
      if len(heap) == 0:
        print(0)
      else:
        print(-heapq.heappop(heap))
    else:
      heapq.heappush(heap, -cur)