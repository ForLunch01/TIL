import statistics

T = int(input())

T_list = []

for i in range(T):
    T_list = (list(map(int, input().split())))
    res = statistics.mean(T_list)
    print(f'#{i+1} {int(round(res, 0))}')