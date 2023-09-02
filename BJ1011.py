import sys
  
TC = int(sys.stdin.readline())

for i in range(TC):
  xy = sys.stdin.readline().split(' ')
  x = int(xy[0])
  y = int(xy[1])

  if (y - x) % 2 == 0:
    print((y - x) // 2 + 1)
  else:
    print((y - x) // 2 + 2)