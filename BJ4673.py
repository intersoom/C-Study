# notSelfNumber = []

# # 각 자릿수의 숫자를 1, 10, 100, 1000의 자리를 구분하여서 구한 후
# for i in range(1, 10000):
#     if i >= 1000:
#         d = i % 10
#         c = (i // 10) % 10
#         b = (i // 100) % 10
#         a = i // 1000
#     elif i >= 100:
#         d = i % 10
#         c = (i // 10) % 10
#         b = i // 100
#         a = 0
#     elif i >= 10:
#         d = i % 10
#         c = i // 10
#         b = 0
#         a = 0
#     elif i > 0:
#         d = i
#         c = 0
#         b = 0
#         a = 0
#     # 셀프넘버가 아닌 숫자들을 구해서 리스트를 만들어준다
#     num = i + a + b + c + d
#     notSelfNumber.append(num)

# # 셀프넘버가 아닌 숫자들의 리스트에 들어있지 않으면 셀프넘버이므로 리스트에 있지 않으면 출력한다
# for i in range(1, 10000):
#     if i in notSelfNumber:
#         continue
#     else:
#         print(i)



## 2트

arr = []

for i in range(1, 10001):
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
    arr.append(a + b + c + d + i)

for i in range(1, 10001):
    if i not in arr:
        print(i)