# 원인: 입력 받은 값이 문자열이므로 int로 형변환이 안됨

# words = list(map(int, input().split()))
words = list(map(str, input().split()))
print(words)