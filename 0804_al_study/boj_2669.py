from itertools import combinations

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

def get_coord(list_ord):
    res_list = []
    for i in range(list_ord[0], list_ord[2]):
        for j in range(list_ord[1], list_ord[3]):
            res_list.append([i, j])
    
    return res_list


final_list = []

final_list.extend(get_coord(A))
final_list.extend(get_coord(B))
final_list.extend(get_coord(C))
final_list.extend(get_coord(D))

new_list = []

for v in final_list:
    if v not in new_list:
        new_list.append(v)
        
print(len(new_list))
