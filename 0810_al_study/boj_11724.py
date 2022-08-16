import sys
sys.setrecursionlimit(5000)

N, M = map(int, input().split())
adj = [[] for i in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)
    
count = 0    
   
for i in range(1, N+1):
    if visited[i] == False:
        count += 1
        dfs(i)


print(count)
    
