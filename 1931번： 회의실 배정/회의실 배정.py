#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1931                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sallybig <boj.kr/u/sallybig>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1931                           #+#        #+#      #+#     #
#    Solved: 2024/07/30 09:55:04 by sallybig      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

num = int(sys.stdin.readline())
arr = []

answer = 0
endPoint = 0

for i in range(num):
    arr.append(list(map(int, sys.stdin.readline().split(' '))))

    arr.sort(key=lambda x: (x[1], x[0]))

    for start, end in arr:
        if endPoint <= start:
            answer += 1
            endPoint = end

print(answer)
