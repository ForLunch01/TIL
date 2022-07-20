T = int(input())

P = [0 for i in range(T)]
Q = [0 for i in range(T)]
R = [0 for i in range(T)]
S = [0 for i in range(T)]
W = [0 for i in range(T)]

for i in range(T):
    P[i], Q[i], R[i], S[i], W[i] = list(map(int, input().split()))


for i in range(T):
    A = P[i] * W[i]
    if W[i] > R[i]:
        B = Q[i] + (W[i]-R[i])*S[i]
    else:
        B = Q[i]
    if A > B:
        print(f'#{i+1} {B}')
    else:
        print(f'#{i+1} {A}')
        