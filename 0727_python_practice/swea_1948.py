T = int(input())

month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    
    sum_day = 0
    
    while m1 != m2:
        x1 = month_day[m1] - d1 + 1
        m1 = m1 + 1
        sum_day = sum_day + x1
        d1 = 1
        
    sum_day = sum_day + (d2 - d1 +1)
    
    print(f"#{i+1}", sum_day)
    
        
        
    