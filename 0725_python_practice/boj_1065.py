def boj_1065():
    N = int(input())
    
    count = 0
    for i in range(1, N+1):
        if i <= 99:
            count += 1
        else:
            count = count + int(is_hansu(i))
            
    print(count)
    return count
        
        
def is_hansu(number):
    numbers = list(map(int, str(number)))
    
    check = True
    
    for i in range(len(numbers)-2):
        if numbers[i]-numbers[i+1] != numbers[i+1] - numbers[i+2]:
            check = False

    return check

boj_1065()
