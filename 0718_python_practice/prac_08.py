word = "HappyHacking"

count = 0

for char in word:
    # or 연산이 char과 비교하고 있지 않아 그냥 true 값이 되어버림
    if char in ["a", "e", "i", "o", "u"]:
        count += 1

print(count)