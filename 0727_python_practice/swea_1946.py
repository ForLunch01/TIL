T = int(input())

for i in range(T):
    case = int(input())
    
    doc = ""
    for j in range(case):
        alpha = input().split()
        doc = doc + alpha[0]*int(alpha[1])
    
    doc_count = 0
    
    
    print(f'#{i+1}')
    for d in doc:
        if doc_count == 10:
            print()
            doc_count = 0
        
        print(d, end="")
        doc_count += 1
        