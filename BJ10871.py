arr = []
inputArr = []
result = []
userInput = input()
arr = userInput.split(' ')

N = int(arr[0])
X = int(arr[1])

userInput = input()
inputArr = userInput.split(' ')

for i in inputArr:
    if int(i) < X:
        result.append(int(i))

for i in result:
    print(i, end=' ')