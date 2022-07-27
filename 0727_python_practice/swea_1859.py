T = int(input())

for i in range(T):
    day_len = int(input())
    d_list = list(map(int, input().split()))

    d_max = d_list[-1]
    sum = 0
    for j in range(day_len-1, -1, -1):
        if d_list[j] < d_max:
            sum = sum + d_max - d_list[j]
        elif d_list[j] > d_max:
            d_max = d_list[j]
    print(f'#{i+1} {sum}')
        