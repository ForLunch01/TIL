number = int(input())

cnt = 1

while number//10:
    if number//10 > 0:
        cnt += 1
        number = number//10

print(cnt)