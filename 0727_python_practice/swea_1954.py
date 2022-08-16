def swea_1954():
    T = int(input())
    
    for i in range(T):
        N = int(input())
        
        snail_list = [[0 for j in range(N)] for k in range(N)]
        count_max = N*N
        go_right(snail_list, 0, 0, 1, count_max)

        print(f'#{i+1}')
        for i in range(N):
            print(*snail_list[i])
        
        
def go_up(li, x, y, count, max): 
    li[x][y] = count

    if x <= 0 or li[x-1][y] != 0:
        if count == max:
            return
        else:
            go_right(li, x, y+1, count+1, max)
    else:
        go_up(li, x-1, y, count+1, max)
    

def go_down(li, x, y, count, max):
    li[x][y] = count
    
    if x+1 >= len(li) or li[x+1][y] != 0:
        if count == max:
            return
        else:
            go_left(li, x, y-1, count+1, max)
    else:
        go_down(li, x+1, y, count+1, max)

def go_left(li, x, y, count, max):
    li[x][y] = count
    
    if y <= 0 or li[x][y-1] != 0:
        if count == max:
            return
        else:
            go_up(li, x-1, y, count+1, max)
    else:
        go_left(li, x, y-1, count+1, max)

def go_right(li, x, y, count, max):
    li[x][y] = count
    
    if y+1 >= len(li) or li[x][y+1] != 0:
        if count == max:
            return
        else:
            go_down(li, x+1, y, count+1, max)
    else:
        go_right(li, x, y+1, count+1, max)

swea_1954()