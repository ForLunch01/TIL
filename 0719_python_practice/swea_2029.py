T = int(input())

T_list = []

for i in range(T):
    T_list.append(list(map(int, input().split())))
    
for idx, t in enumerate(T_list):
    print("#"+str(idx+1), *divmod(t[0], t[1]))