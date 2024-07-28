#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1436                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sallybig <boj.kr/u/sallybig>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1436                           #+#        #+#      #+#     #
#    Solved: 2024/07/28 15:05:48 by sallybig      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

input = int(sys.stdin.readline())

count = 0
i = 1
result = 0

while count != input:
    if '666' in str(i):
        count += 1
        result = i
    i += 1
print(result)
