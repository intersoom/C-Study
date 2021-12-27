count, kill = input().split(" ")

count = int(count)
kill = int(kill)

peopleList = []
result = []
killCount = 1

for i in range(1, count+1):
        peopleList.append(i)

while len(peopleList) != 0:
    if killCount % kill == 0:
        result.append(peopleList[0])
        del peopleList[0]
    else:
        peopleList.append(peopleList[0])
        del peopleList[0]
    killCount += 1
    
resultStr = "<"

for i in result:
    if result.index(i) < len(result) - 1:
        resultStr = resultStr + (str(i) + ", ")
    else:
        resultStr = resultStr + str(i)
resultStr += ">"

print(resultStr)