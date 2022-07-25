A, B = map(int, input().split())

def GBB(X, Y):
    if X == 1 and Y == 2:
        print("B")
    elif X == 2 and Y == 1:
        print("A")
    elif X == 1 and Y == 3:
        print("A")
    elif X == 3 and Y == 1:
        print("B")
    elif X == 2 and Y == 3:
        print("B")
    elif X == 3 and Y == 2:
        print("A")
        
GBB(A, B)