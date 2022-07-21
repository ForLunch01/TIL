# 민석이는 양 세기,
# N의 배수 번호인 양을 세기
# N, 2N, ..., kN
# 이전에 셌던 번호들의 각 자리수에서
# 0~9까지 모든 숫자를 보는 것은 최소 몇 번 양?

# n의 배수를 읽어나가며 그 각 자리수를 리스트에 더하고
# 그게 0~9인 첫번째 경우

# 구현
# set check 0 ~ 9 이면 true
# while true: 문 사용
# n이 될 때마다 str int로 집어넣음

T = int(input())

for i in range(T):
    t = int(input())
    j = 1
    num_set = set()
    while True:
        sheep = j*t
        num_set.update(str(sheep))
        
        if len(num_set) == 10:
            print(f"#{i+1} {j*t}")
            break
        j = j+1

        
        