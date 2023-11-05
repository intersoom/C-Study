import sys

N, M = map(int, sys.stdin.readline().split(' '))
arr = []


def backtrack():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    else:
        for i in range(1, N+1):
            if i not in arr:
                arr.append(i)
                backtrack()
                arr.pop()


backtrack()
