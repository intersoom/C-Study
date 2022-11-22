user = int(input())
count = 0

def rule(x):
    print(x)
    if x % 3 == 1:
        return x - 1
    elif x % 2 == 0:
        return x // 2
    else:
        return x - 1

hello = int(user)

while hello > 1:
    count += 1
    hello = rule(hello)


print(count)
