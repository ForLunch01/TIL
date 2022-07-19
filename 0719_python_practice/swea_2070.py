T = int(input())

T_list = []

for i in range(T):
    T_list.append(list(map(int, input().split())))
    
for i in range(T):
    if T_list[i][0] < T_list[i][1]:
        print(f'#{i+1} <')
    elif T_list[i][0] == T_list[i][1]:
        print(f'#{i+1} =')
    elif T_list[i][0] > T_list[i][1]:
        print(f'#{i+1} >')