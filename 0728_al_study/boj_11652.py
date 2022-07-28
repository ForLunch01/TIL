import sys

input = sys.stdin.readline

N = int(input())

N_dict = dict()

for i in range(N):
    num_input = int(input())
    if num_input in N_dict:
        N_dict[num_input] += 1
    else:
        N_dict[num_input] = 1
    
max_val = max(N_dict.values())

print(max_val)
# for k, v in N_dict.items():
    
    
    