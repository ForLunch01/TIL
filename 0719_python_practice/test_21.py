N = int(input())
N_list = []

while N != 0:
    x, y = divmod(N, 10)
    N = x
    N_list.append(y)

N_list = list(map(str, N_list))
print(int("".join(N_list)))

