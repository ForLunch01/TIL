h, b, c, s = map(int, input().split())

b = h*b*c*s/8

mb = b/1024/1024

print(f'{mb:.1f}', 'MB')