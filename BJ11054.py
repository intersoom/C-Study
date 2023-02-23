from sys import stdin

T = int(stdin.readline())
arr = stdin.readline().split(' ')

N = []
right = []
left = []
rightAndLeft = []

for i in arr:
    N.append(int(i))

    right.append(1)
    left.append(1)

for i in range(T):
    for j in range(i):
        if N[i] > N[j]:
            right[i] = max(right[i], right[j] + 1)

N.reverse()

for i in range(T):
    for j in range(i):
        if N[i] > N[j]:
            left[T - i - 1] = max(left[T - i - 1], left[T - j - 1] + 1)

for i in range(T):
    rightAndLeft.append(right[i] + left[i] - 1)

print(max(rightAndLeft))