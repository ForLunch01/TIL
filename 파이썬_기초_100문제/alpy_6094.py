n = int(input())
a = list(map(int, input().split()))

d = [0 for i in range(n)]

for i in range(n):
    d[i] = a[i]
    
print(min(d))