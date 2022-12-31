sugar = int(input())
result = 0

while sugar >= 0:
    # 5의 배수면 5로 나눠서 그 수를 결과 값에 더해서 출력 (처음 숫자가 5인 경우 또는 3을 빼서 5의 배수가 된 경우)
    if sugar % 5 == 0:
        result += (sugar // 5)
        print(result)
        break
    # 5의 배수가 아닌 경우, 0이 될 때까지 3을 빼주며 result에 1씩 더해줌
    sugar -= 3
    result += 1
# 3으로 빼서 0 미만인 경우, 정확하게 N킬로그램을 만들 수 없기 때문에 -1 출력
else:
    print(-1)
