T_list = [[] for i in range(5)]

for i in range(5):
    T_list[i] = input()
    
for i in range(15):
    
    for j in range(5):
        if len(T_list[j]) > i:
            print(T_list[j][i], end="")