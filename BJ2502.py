from sys import stdin

user = stdin.readline()
days = int(user.split()[0])
riceCakes = int(user.split()[1])

result = []

# A 갯수: [0], B 갯수: [1]
AB = [[0, 0] for _ in range(days)]
AB[0] = [1, 0]
AB[1] = [0, 1]

# 첫 날이 0
for i in range(2, days):
    AB[i][0] = AB[i - 1][0] + AB[i - 2][0]
    AB[i][1] = AB[i - 1][1] + AB[i - 2][1]

countA = AB[days - 1][0]
countB = AB[days - 1][1]

for i in range(riceCakes):
    if (riceCakes - countB * i) % countA == 0 and (riceCakes - countB * i) // countA <= i:
        print((riceCakes - countB * i) // countA)
        print(i)
        break