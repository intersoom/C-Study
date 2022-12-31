# 그냥 input으로 받으니까 시간초과 나서 stdin 라이브러리 사용함 (readline()이 input과 같은 역할)
from sys import stdin

count = int(stdin.readline())

command = [''] * count
stack = []

# 처음에 입력 받은 명령어의 개수만큼 for문을 돌려서 명령어 실행함
for i in range(count):
    command = stdin.readline()
    # 문지열에 명령어 포함여부를 판단해서 명령 실행
    if 'push' in command:
        # split 이용하여 띄어쓰기 구분해서 push할 숫자 구분하여서 stack 리스트에 push함
        temp = command.split(' ')
        stack.append(int(temp[1]))
    elif 'top' in command:
        # 길이가 0인 경우, -1 출력하고
        if len(stack) == 0:
            print(-1)
        # 아닌 경우에 index -1 이용해서 맨 뒤의 인덱스의 값을 출력함
        else:
            print(stack[-1])
    elif 'size' in command:
        # 리스트 크기 알려주는 len함수 이용해서 size 출력
        print(len(stack))
    elif 'empty' in command:
        # 길이가 0인 경우 1 출력
        if len(stack) == 0:
            print(1)
        # 아닌 경우 0 출력
        else:
            print(0)
    elif 'pop' in command:
        # 리스트 길이 0인 경우 -1 출력
        if len(stack) == 0:
            print(-1)
        # 아닌 경우 pop함수 이용해서 pop하고 해당 숫자 print
        else:
            print(stack.pop())