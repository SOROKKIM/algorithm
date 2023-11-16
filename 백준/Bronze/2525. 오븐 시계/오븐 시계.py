H, M = map(int, input().split())
T = int(input())

H += T //60
M += T %60

if M >= 60:
    H += 1
    print(H%24, M-60)
else:
    print(H%24, M)