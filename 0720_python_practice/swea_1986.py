T = int(input())
T_list = []
for t in range(T):
    T_list.append(int(input()))
    
for idx, t in enumerate(T_list):
    sum = 0
    for i in range(1, t+1):
        if i % 2 != 0:
            sum = sum + i
        else:
            sum = sum - i
    print(f'#{idx+1} {sum}')