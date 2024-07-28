#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4673                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sallybig <boj.kr/u/sallybig>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4673                           #+#        #+#      #+#     #
#    Solved: 2024/07/28 14:31:10 by sallybig     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
result = []

for i in range(1, 10000):
    result.append(i)

for i in range(9999, 0, -1):

    stringInt = str(i)

    sum = int(i)
    for k in stringInt:
        sum += int(k)
    if sum in result:
        result.remove(sum)

for i in result:
    print(i)
