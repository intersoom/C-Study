import sys

N = int(sys.stdin.readline())
users = []

for i in range(N):
  users.append(sys.stdin.readline())
  
users.sort(key=lambda x : (int(x.split(' ')[0])))

for i in users:
  print(i, end='')
