T = int(input())

def get_alpha(number, num):
    alpha = 0
    
    while True:
        if number % num == 0:
            number = number // num
            alpha = alpha + 1
        else:
            return alpha
        

for i in range(T):
    N = int(input())
    a = get_alpha(N, 2)
    b = get_alpha(N, 3)
    c = get_alpha(N, 5)
    d = get_alpha(N, 7)
    e = get_alpha(N, 11)
    print(f'#{i+1}', a, b, c, d, e)

