import copy

def swea_1961():
    T = int(input())
    
    for i in range(T):
        mat_len = int(input())
        a = [[0 * mat_len] for i in range(mat_len)]
        a_90 = [[0 * mat_len] for i in range(mat_len)]
        a_180 = [[0 * mat_len] for i in range(mat_len)]
        a_270 = [[0 * mat_len] for i in range(mat_len)]
        
        for j in range(mat_len):
            a[j] = list(map(int, input().split()))
        
        a_90 = rotate_90(a)
        a_180 = rotate_90(a_90)
        a_270 = rotate_90(a_180)
        
        print(f'#{i+1}')
        for k in range(mat_len):
            print("".join(map(str, a_90[k])), end = " ")
            print("".join(map(str, a_180[k])), end = " ")
            print("".join(map(str, a_270[k])), end = " ")
            print()
            
def rotate_90(mat):
    N = len(mat)
    new_mat = copy.deepcopy(mat)
    for i in range(N):
        for j in range(N):
            new_mat[i][j] = mat[(N-1-j)%N][i]
    
    return new_mat
        
swea_1961()
