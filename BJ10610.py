import sys

userInput = sorted(
    list(map(int, list(sys.stdin.readline().replace("\n", "")))), reverse=True)

if 0 not in userInput or not sum(userInput) % 3 == 0:
    print(-1)
else:
    print(''.join(list(map(str, userInput))))
