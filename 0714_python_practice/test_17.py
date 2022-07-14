word = input()

for w in word:
    if w.islower():
        w_ord = ord(w)
        w_ord_upper = w_ord - 32
        w_upper = chr(w_ord_upper)
        print(w_upper, end="")