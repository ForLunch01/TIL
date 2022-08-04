N = int(input())

room = [[] for i in range(N)]

for i in range(N):
    room[i] = list(input())


count_pos1 = 0
for i in range(N):
    count_row = 0
    for j in range(N):
        if room[i][j] == '.':
            count_row += 1
            
            if count_row == 2:
                count_pos1 += 1
            
        if room[i][j] == 'X':
            count_row = 0

new_room = [['_' for i in range(N)]  for j in range(N)]

for i in range(N):
    for j in range(N): 
        new_room[j][N-i-1] = room[i][j]


count_pos2 = 0
for i in range(N):
    count_col = 0
    for j in range(N):
        if new_room[i][j] == '.':
            count_col += 1
            
            if count_col == 2:
                count_pos2 += 1
                
        if new_room[i][j] == 'X':
            count_col = 0

print(count_pos1, count_pos2)
    
            
        
    