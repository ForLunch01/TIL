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