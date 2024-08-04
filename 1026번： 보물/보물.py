#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1026                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sallybig <boj.kr/u/sallybig>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1026                           #+#        #+#      #+#     #
#    Solved: 2024/08/04 17:51:00 by sallybig      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' ')))
B = list(map(int, sys.stdin.readline().split(' ')))

A.sort()
B.sort(reverse=True)

sum = 0

for n in range(N):
    sum += (A[n] * B[n])

print(sum)
