import sys

sys.stdin = open("swea_1204_input.txt", "r")

T = int(input())

for i in range(T):
    num_dict = dict()
    case_num = int(input())
    numbers = list(map(int, input().split()))
    
    for n in numbers:
        if num_dict.get(n):
            num_dict[n] += 1
        else:
            num_dict[n] = 1

    max_value = max(num_dict.values())
    max_num_list = []
    
    for k, v in num_dict.items():
        if v == max_value:
            max_num_list.append(k)
    
    print(f'#{i+1} {max(max_num_list)}')