T = list(map(int, input().split()))

ascending_check = True
descending_check = True
for i in range(len(T)-1):
    if T[i] > T[i+1]:
        ascending_check = False
    elif T[i] < T[i+1]:
        descending_check = False
        
if ascending_check == True:
    print("ascending")
elif descending_check == True:
    print("descending")
else:
    print("mixed")
    