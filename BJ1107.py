# 1) 100 기준으로 움직임
# 2) 숫자 버튼 눌러서 이동 후,( + / - 버튼 눌러서 이동)

possibleNum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
channel = input()
intChannel = int(channel)
brokenCount = int(input())

if brokenCount > 0:
    brokenNum = input()
    brokenNumList = brokenNum.split(' ')
    for i in brokenNumList:
        possibleNum.remove(int(i))

for i in possibleNum:
    i = str(i)

min = 0

# 1) 100 기준으로 움직임
min = int(channel) - 100
if min < 0:
    min = -min

# 2) 숫자 버튼 눌러서 이동 후, (+ / - 버튼 눌러서 이동)
isOk = True
plusBtn = 0

while True:
    intChannel += 1
    plusBtn += 1
    channel = str(intChannel)
    count = 0
    for i in channel:
        if channel in possibleNum:
            count += 1
    if count == len(channel):
        break

if min > len(channel) + plusBtn:
    min = len(channel) + plusBtn

print(min)

