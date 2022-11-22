count, kill =  input().split(" ")
count = int(count)
kill = int(kill)

result = []
keep = []

killCount = 0
index = kill -1


peopleList = list(map(int, range(1, count+1)))
keep = peopleList

for i in range(count):
    result.append(str(peopleList[index]))
    keep.pop(index)
    
    index += kill
    
    if index >= len(peopleList):
        index = index - len(peopleList)
        
        
            
        
# 출력 파트
resultStr = "<"
resultStr += ", ".join(result)
resultStr += ">"

print(resultStr)