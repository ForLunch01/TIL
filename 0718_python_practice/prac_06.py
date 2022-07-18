# tuple은 immutable, 변형 불가능하므로 append 할 수 없음

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)