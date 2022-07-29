from operator import mul
def swea_1959():
    T = int(input())
    
    for i in range(T):
        N, M = map(int, input().split())
        A_list = list(map(int, input().split()))
        B_list = list(map(int, input().split()))
        
        if len(A_list) > len(B_list):
            res = get_max_sum(A_list, B_list)
        else:
            res = get_max_sum(B_list, A_list)
            
        print(f'#{i+1} {res}')
        
            
def get_max_sum(list_A, list_B):
    range_len = len(list_A) - len(list_B)
    max_value = sum(map(mul, list_B, list_A[:len(list_B)]))
    for i in range(1, range_len+1):
        value = sum(map(mul, list_B, list_A[i:i+len(list_B)]))
        if value > max_value:
            max_value = value
    
    return max_value
    
swea_1959()