userInput = input().split(' ')
a = int(userInput[0])
b = int(userInput[1])

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def lcm(a, b):
  return a // gcd(a, b) * b

print(gcd(a, b))
print(lcm(a, b))