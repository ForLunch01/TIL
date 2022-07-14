# word list 초기화
words = ['apple', 'banana', 'kiwi']

# word list 길이 만큼 a의 위치를 셀 idx_a 리스트 초기화
idx_a = [0 for i in range(len(words))]

for w_idx, w in enumerate(words):
    # word의 문자 하나 마다
    # enumerate를 활용해 문자열 내 문자(c)와 그 인덱스(c_idx)를 받아옴
    for c_idx, c in enumerate(w):
        # c == 'a' 이면
        if c == 'a':
            idx_a[w_idx] = c_idx
            # a를 찾았으면 for문 중단
            break
    # for-else 문으로 for문을 모두 돌아도 a를 못 찾으면 -1 입력    
    else:
        idx_a[w_idx] = -1
        
for i in range(len(words)):
    print(words[i], idx_a[i], sep =': ')