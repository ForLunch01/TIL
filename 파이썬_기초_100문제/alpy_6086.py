n = int(input())

s = 1
sum = 0

while True:
    sum += s
    if sum >= n:
        print(sum)
        break
    s = s+1