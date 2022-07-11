n = int(input())
a = 1
sum = 0

while sum <= n:
    sum = sum + a
    
    if sum >= n:
        print(a)
        break
    
    a = a + 1
    