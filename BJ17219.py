import sys

dict = {}

NM = sys.stdin.readline().split(' ')
N = int(NM[0])
M = int(NM[1])

for i in range(N):
  userInput = sys.stdin.readline().split(' ')
  dict[userInput[0].replace('\n', '')] = userInput[1].replace('\n', '')

for i in range(M):
  userInput = sys.stdin.readline().replace('\n', '')
  print(dict[userInput])