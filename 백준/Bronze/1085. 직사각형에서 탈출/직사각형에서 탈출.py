x, y, w, h = map(int, input().split())
A = 0
B = 0
if (w-x) < x:
    A = w-x
else:
    A = x
if (h-y) < y:
    B = h-y
else:
    B = y
if A < B:
    print(A)
else:
    print(B)