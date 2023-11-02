import sys

NM = list(map(int, sys.stdin.readline().split(' ')))
N = NM[0]
M = NM[1]
pokemon = {}
pokemon2 = {}

for i in range(N):
    poke = sys.stdin.readline().replace('\n', '')
    pokemon[i+1] = poke
    pokemon2[poke] = i+1

for i in range(M):
    question = sys.stdin.readline().replace('\n', '')
    if question.isnumeric():
        print(pokemon[int(question)])
    else:
        print(pokemon2[question])
