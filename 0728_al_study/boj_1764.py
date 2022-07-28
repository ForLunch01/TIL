import sys

input = sys.stdin.readline

N, M = map(int, input().split())

n_dict = dict()
m_dict = dict()

for i in range(N):
    input_str = input().strip()
    n_dict[input_str] = 1
    
for j in range(M):
    input_str = input().strip()
    m_dict[input_str] = 1
    
n_m_list = []

for n in n_dict:
    if n in m_dict:
        n_m_list.append(n)

n_m_list.sort()
print(len(n_m_list))

for nm in n_m_list:
    print(nm)

