notSelfNumber = []

for i in range(1, 10000):
    if i >= 1000:
        d = i % 10
        c = (i // 10) % 10
        b = (i // 100) % 10
        a = i // 1000
    elif i >= 100:
        d = i % 10
        c = (i // 10) % 10
        b = i // 100
        a = 0
    elif i >= 10:
        d = i % 10
        c = i // 10
        b = 0
        a = 0
    elif i > 0:
        d = i
        c = 0
        b = 0
        a = 0
    num = i + a + b + c + d
    notSelfNumber.append(num)

for i in range(1, 10000):
    if i in notSelfNumber:
        continue
    else:
        print(i)
