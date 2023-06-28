testCase = int(input())
inputArr = []

for i in range(0, testCase):
  inputArr.append(int(input()))

resultArr = [0] * 11
resultArr[1] = 1
resultArr[2] = 2
resultArr[3] = 4

for input in inputArr:
  for k in range(4, input + 1):
    resultArr[k] = resultArr[k - 1] + resultArr[k - 2] + resultArr[k - 3]

  print(resultArr[input])