T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    c, d = divmod(a, b)
    
    print(f'#{i+1} {c} {d}')