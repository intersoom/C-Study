import sys

i = int(sys.stdin.readline())
count = 0

for i in range(1, i + 1):
  if i == 1000:
    continue
  elif i >= 100:
    d = i % 10
    c = (i // 10) % 10
    b = i // 100
    a = 0
    if b - c == c - d:
      count += 1
  elif i >= 10:
    count += 1
  elif i > 0:
    count += 1

print(count)