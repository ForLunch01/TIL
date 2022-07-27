def swea_1940():
    T = int(input())
    for i in range(T):
        
        case_num = int(input())
        case_list = []
        distance = 0
        accel = 0
        for j in range(case_num):
            case_list.append(list(map(int, input().split())))
            
            if case_list[j][0] == 0:
                distance = distance + accel
                
            elif case_list[j][0] == 1:
                accel = accel + case_list[j][1]
                distance = distance + accel
            
            elif case_list[j][0] == 2:
                accel = accel - case_list[j][1]
                if accel < 0:
                    accel = 0
                distance = distance + accel
            
        print(f'#{i+1} {distance}')

swea_1940()