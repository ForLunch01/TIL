import sys

input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_dict = dict()
for i in range(N):
    if N_dict.get(N_list[i]):
        N_dict[N_list[i]] += 1
    else:
        N_dict[N_list[i]] = 1
        
M = int(input())
M_list = list(map(int, input().split()))
for j in range(M):
    if N_dict.get(M_list[j]):
        print(N_dict.get(M_list[j]), end=" ")
    else:
        print(0, end=" ")
 
 #################################################3
        
import sys

input = sys.stdin.readline

M = int(input())
m_list = []
m_list.extend(list(map(int, input().split())))
N = int(input())
n_list = []
n_list.extend(list(map(int, input().split())))
n_dict = {}

for m in m_list:
    if m in n_dict:
        n_dict[m] += 1
    else:
        n_dict[m] = 1
        
for i in n_list:
    if i in n_dict:
        print(n_dict[i], end=" ")
    else:
        print(0, end=" ")