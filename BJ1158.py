count, kill =  input().split(" ")
count = int(count)
kill = int(kill)

result = []

killCount = 1
index = 0
endIndex = count

#peopleList = list(map(int, range(1, count+1)))

while count != 0:
    if index == endIndex:
        index = 0
            
    if str((index + 1)) not in result:
        if killCount == kill:
            print(index)
            result.append(str(index + 1))
            killCount = 1
            count -= 1
        else:
            killCount += 1
    index += 1
     
        
# 출력 파트
resultStr = "<"
resultStr += ", ".join(result)
resultStr += ">"

print(resultStr)