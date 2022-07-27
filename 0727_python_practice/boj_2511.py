A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_sum = 0
B_sum = 0
last_win = ""
for i in range(10):
    if A_list[i] > B_list[i]:
        A_sum += 3
        last_win = "A"
    elif A_list[i] < B_list[i]:
        B_sum += 3
        last_win = "B"
    else:
        A_sum +=1
        B_sum +=1
        
print(A_sum, B_sum)

if A_sum > B_sum:
    print("A")
elif A_sum < B_sum:
    print("B")
else:
    print("D")