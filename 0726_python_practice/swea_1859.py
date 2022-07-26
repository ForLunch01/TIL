# 1. 연속된 N일 동안의 물건 매매가를 안다.
# 2. 하루에 최대 1만큼 구입 가능하다.
# 3. 판매는 얼마든지 할 수 있다.

T = int(input())

for t in range(T):
    day_length = int(input())
    day_list = list(map(int, input().split()))
    sum = 0
    next_max_index = -1
    
    for i in range(day_length-1):
        if i == next_max_index or next_max_index == -1:
            next_max = max(day_list[i+1:])
            next_max_index = day_list[i+1:].index(next_max)+i+1
        
        if day_list[i] < next_max:
            sum = sum + next_max - day_list[i]
    
    print(f'#{t+1} {sum}')
        
            
        