N = int(input())

a, b = map(int, str(N))
new_N = b*10 + a+b
cycle = 1

while N != new_N:
    if new_N < 10:
        new_N = new_N * 10
    a, b = map(int, str(new_N))
    c = 0
    if a+b > 10:
        c = a + b -10
    else:
        c = a + b
    new_N = b*10 + c
    cycle += 1
    
print(cycle)

N = int(input())

# 26일 때, 2+6은 8
# 그렇다면 새로운 수는 68


a, b = divmod(N, 10)
c, d = divmod(a+b, 10)

cycle_N = 10*b+d
count = 1

while cycle_N != N:
    a, b = divmod(cycle_N, 10)
    c, d = divmod(a+b, 10)
    cycle_N = 10*b+d
    count += 1

print(count)