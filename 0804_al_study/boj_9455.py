def get_y_box(grid, y, x, M):
    count = 0
    for i in range(y+1, M):
        if grid[i][x] == 0:
            count += 1
    
    return count

T = int(input())

for i in range(T):
    M, N = map(int, input().split())
    
    grid = [[0 for i in range(N)] for i in range(M)]
    
    for i in range(M):
        grid[i] = list(map(int, input().split()))
    
    count = 0
    
    for y in range(M):
        for x in range(N):
            if grid[y][x] == 1:
                count += get_y_box(grid, y, x, M)
    
    print(count)
                


                