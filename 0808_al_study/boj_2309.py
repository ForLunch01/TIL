from itertools import combinations

s_list = []

for i in range(9):
    s_list.append(int(input()))
    
cb = combinations(s_list, 7)

res_list = []

for c in cb:
    if sum(c) == 100:
        res_list = list(c)

res_list.sort()

for r in res_list:
    print(r)
    


    