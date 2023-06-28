def factorization(num):
    div = 2
    while num == 1:
        if num % div == 0:
            num = num / div
        else:
            div += 1
    return num

a, b, c, d, e = input().split(" ")

a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

