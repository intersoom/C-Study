inputCount = int(input())
studentInfos = []

for i in range(inputCount):
    studentInfo = input().split(' ')
    name = studentInfo[0]
    kor = int(studentInfo[1])
    eng = int(studentInfo[2])
    math = int(studentInfo[3])
    studentInfos.append((name, kor, eng, math))

studentInfos.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in studentInfos:
    print(i[0])
