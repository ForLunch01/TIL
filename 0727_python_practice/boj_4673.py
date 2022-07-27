
comp_list = []
for i in range(1, 10000):
    comp_list.append(i + sum(map(int, str(i))))

for i in range(1, 10000):
    if i not in comp_list:
        print(i)
