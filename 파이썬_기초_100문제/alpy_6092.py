n = int(input())
a = list(map(int, input().split()))

d = []

for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

d.pop(0)

print(*d)