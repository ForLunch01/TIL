# word list 초기화
words = ['HappyHacking', 'banana', 'kiwi']

# word list 길이 만큼 a들의 위치를 셀 idx_a_list 이차원 리스트 초기화
idx_a_list = [[] for i in range(len(words))]

for w_idx, w in enumerate(words):
    # word의 문자 하나 마다
    # enumerate를 활용해 문자열 내 문자(c)와 그 인덱스(c_idx)를 받아옴
    for c_idx, c in enumerate(w):
        # c == 'a' 이면
        if c == 'a':
            # words 인덱스에 맞는 idx_a_list에 a를 찾을 때마다 append
            idx_a_list[w_idx].append(c_idx)
            
for i in range(len(words)):
    print(words[i] + ' #', *idx_a_list[i])