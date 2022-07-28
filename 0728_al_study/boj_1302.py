import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

N_list = []
for i in range(N):
    N_list.append(input().strip())
    
N_list.sort()   
print(Counter(N_list).most_common(1)[0][0])



    
