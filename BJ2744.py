userInput = input()
result = ''

for i in userInput:
    if i.isupper():
        result += i.lower()
    else:
        result += i.upper()

print(result)
