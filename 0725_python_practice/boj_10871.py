N, X = map(int, input().split())
N_list = map(int, input().split())

for n in N_list:
    if n < X:
        print(n, end=" ")
