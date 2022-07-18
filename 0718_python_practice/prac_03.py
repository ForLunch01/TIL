# 원인: input()의 반환값은 str형이기에 sum 연산이 불가능

# numbers = input().split()
numbers = map(int, input().split())
print(sum(numbers))