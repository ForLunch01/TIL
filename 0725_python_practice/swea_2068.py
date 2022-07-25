T = int(input())

for i in range(T):
    num_list = map(int, input().split())
    print(f'#{i+1} {max(num_list)}')