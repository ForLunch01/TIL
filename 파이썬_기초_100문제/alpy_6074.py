c = ord(input())
a_num = ord('a')

c_list = []

for i in range(a_num, c+1):
    c_list.append(chr(i))

print(*c_list)