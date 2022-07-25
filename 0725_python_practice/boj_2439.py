def boj2439():
    N = int(input())
    
    for i in range(1, N+1):
        star = '*'*i
        print(f'{star:>{N}}')

boj2439()