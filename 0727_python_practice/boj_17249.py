T = input()

T = T.replace("=", "")

T_L, T_R = T.split("(^0^)")

print(len(T_L), len(T_R))