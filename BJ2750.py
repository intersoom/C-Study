count = int(input())
arr = []

for i in range(count):
    temp = input()
    arr.append(int(temp))

arr.sort()

for i in arr:
    print(i)