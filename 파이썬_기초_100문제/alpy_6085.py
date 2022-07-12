w, h, b = map(int, input().split())

c1 = w*h*b/8

c2 = c1/1024/1024

print(f'{c2:.2f}', 'MB')