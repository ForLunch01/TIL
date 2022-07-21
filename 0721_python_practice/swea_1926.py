# 369 게임
# 3,6,9가 들어간 수는 말하지 않음

N = int(input())

for i in range(1, N+1):
    if "3" in str(i) or "6" in str(i) or "9" in str(i)   :
        i = str(i).replace("3", "-")
        i = str(i).replace("6", "-")
        i = str(i).replace("9", "-")
        
    if "-" in str(i):
        i.count("-")
        print("-"*i.count("-"), end=" ")
    else:
        print(i, end=" ")