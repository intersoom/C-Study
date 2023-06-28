from collections import deque
userInput = input()
userArr = []
result = []

for i in range(int(userInput)):
    userArr.append(i + 1)
userArr.reverse()
queue = deque(userArr)

count = 0


while queue:
    count += 1
    if len(queue) == 1:
        result.append(queue[0])
        break

    if count % 2 != 0:
        temp = queue.pop()
        result.append(temp)
    else:
        temp = queue.pop()
        queue.appendleft(temp)

for i in result:
    print(i, end=" ")