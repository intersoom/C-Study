import sys

N = int(sys.stdin.readline())

dict = {}
result = []

for i in range(N):
  userInput = sys.stdin.readline().split(' ')

  name = userInput[0]
  entry = userInput[1].replace('\n', '')

  dict[name] = entry

for key, value in dict.items():
  if value == 'enter':
    result.append(key)

result.sort(reverse=True)
for i in result:
  print(i)