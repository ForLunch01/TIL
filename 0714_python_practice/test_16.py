word = input()

vowel_list = ['a', 'e', 'i', 'o', 'u']

count = 0
for w in word:
    if w in vowel_list:
        count += 1
        
print(word + " #", count)