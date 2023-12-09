A, B, V = map(int, input().split())
X = (V-B)%(A-B)
day = (V-B)/(A-B)
if X == 0 :
    print(int(day))
elif X != 0:
    print(int(day)+1)