def check_day(m):
    if int(m) == 2:
        return 28
    elif int(m) in [4, 6, 9, 11]:
        return 30
    else:
        return 31

T = int(input())

for i in range(T):
    case = input()
    
    res = case[0:4]+"/"
    
    if 1 <= int(case[4:6]) <= 12:
        res = res + case[4:6]+"/"
    else:
        res = -1
        print(f'#{i+1} {res}')
        continue
        
    if 1 <= int(case[6:8]) <= check_day(case[4:6]):
        res = res + case[6:8]
    else:
        res = -1
        print(f'#{i+1} {res}')
        continue
    
    print(f'#{i+1} {res}')
        
    

    