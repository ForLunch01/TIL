T = int(input())

for i in range(T):
    t = input().strip()
    
    if t == t[::-1]:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")