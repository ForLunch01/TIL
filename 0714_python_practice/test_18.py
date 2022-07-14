word = input()

word_dict = {}

# 입력 문자열의 문자에 대해 for문
for w in word:
    # w가 이미 사전의 key 안에 있다면
    if w in word_dict.keys():
        # 해당 키에 대한 벨류값 +1
        word_dict[w] += 1
    # w가 사전에 없는 값이라면
    else:
        # 해당 (key : w, value : 1)로 새로 추가
        word_dict[w] = 1
        
for k, v in word_dict.items():
    print(k, v)