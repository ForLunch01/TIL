import sys

input = sys.stdin.readline

N = int(input())

name_dict = dict()

for i in range(N):
    name, log = input().split()
    
    name_dict.update({name : log})

name_list = []
for k, v in name_dict.items():
    if v == "enter":
        name_list.append(k)
        
name_list.sort(reverse=True)

for n in name_list:
    print(n)