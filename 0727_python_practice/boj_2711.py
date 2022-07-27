T = int(input())

for i in range(T):
    miss_spell, word = input().split()
    miss_spell = int(miss_spell)
    
    for i, c in enumerate(word):
        if i+1 != miss_spell:
            print(c, end="")
    print()
