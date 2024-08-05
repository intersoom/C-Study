#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1946                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sallybig <boj.kr/u/sallybig>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1946                           #+#        #+#      #+#     #
#    Solved: 2024/08/04 18:22:28 by sallybig      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    apply = []
    result = []

    for n in range(N):
        apply.append(list(map(int, sys.stdin.readline().split(' '))))

    if len(apply) == 1:
        print(1)
        continue

    aSort = list(sorted(apply, key=lambda x: x[0]))
    max = aSort[0]

    for a in aSort:
        if max[1] >= a[1]:
            max = a
            result.append(a)

    print(len(result))
