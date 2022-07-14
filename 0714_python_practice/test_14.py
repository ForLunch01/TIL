# word list 초기화
words = ['apple', 'banana', 'kiwi']

# word list 길이 만큼 a의 수를 셀 count_a 리스트 초기화
count_a = [0 for i in range(len(words))]

# words 리스트의 index와 word 값 마다
for idx, w in enumerate(words):
    # word의 문자 하나 마다
    for c in w:
        # c == 'a' 이면
        if c == 'a':
            # words 리스트와 count_a 리스트는 길이가 같음
            # 따라서 각 단어에 해당하는 count_a에 1씩 더함
            count_a[idx] += 1
            
for i in range(len(words)):
    print(words[i], count_a[i], sep =': ')
    