# 신용카드는 룬 공식을 만족해야한다.
# 룬 공식이란 카드 번호에서 마지막(16)번째 숫자 N을 구하는 공식.

T = int(input())

for j in range(T):
    num_list = list(map(int, input().split()))
    sum = 0
    for i, n in enumerate(num_list):
        # 홀수면
        if i % 2 == 0:
            sum = sum + (n*2)
        
        # 짝수면
        if i % 2 == 1:
            sum = sum + n
        
    N = (10 - (sum%10)) % 10
    print(f'#{j+1} {N}')
        
        