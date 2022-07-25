T = int(input())

for i in range(T):
    num_list = map(int, input().split())
    
    sum = 0
    
    for num in num_list:
        if num % 2 == 1:
            sum = sum + num
            
    print(f'#{i+1} {sum}')