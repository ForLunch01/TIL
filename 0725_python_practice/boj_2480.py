num_list = [0*3]
num_list = list(map(int, input().split()))

num_dict = dict()

for i in range(len(num_list)):
    num_dict[num_list[i]] = 0
    
for i in range(len(num_list)):
    num_dict[num_list[i]] += 1

count = max(num_dict.values())

if count == 3:
    for k, v in num_dict.items():
        if v == 3:
            print(k*1000+10000)
            break

if count == 2:
    for k, v in num_dict.items():
        if v == 2:
            print(k*100+1000)
            break
if count == 1:
    print(max(num_dict)*100)