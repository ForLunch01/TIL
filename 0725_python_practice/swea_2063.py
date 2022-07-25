from ast import Index


N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

index = int((N-1)/2)
print(N_list[index])