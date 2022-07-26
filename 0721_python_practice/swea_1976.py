# 시 분으로 이루어진 시각을 2개 입력 받음
# 더한 값을 시 분으로 출력

# 시간은 12 이상이면 1로 바꿈
# 분은 60 이상이면 60을 빼고 시간에 1을 더함


T = int(input())

for t in range(T):
    H1, M1, H2, M2 = map(int, input().split())
    
    H3 = H1 + H2
    if H3 > 12:
        H3 = H3 - 12
        
    M3 = M1+M2
    if M3 >= 60:
        M3 = M3 - 60
        H3 = H3 + 1
    
    print(f'#{t+1} {H3} {M3}') 