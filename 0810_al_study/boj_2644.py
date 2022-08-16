import sys
sys.setrecursionlimit(100000)

N = int(input())
c1, c2 = map(int, input().split())
M = int(input())

c_graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
c_count = [0] * (N+1)

for i in range(M):
    x, y = map(int, input().split())
    
    c_graph[x].append(y)
    c_graph[y].append(x)

def dfs(v):
    visited[v] == True
    for i in c_graph[v]:
        if visited[i] == False:
            c_count[i] = c_count[v] + 1
            dfs(i)
            
print(c_graph)            
    
dfs(c1)

print(visited)


