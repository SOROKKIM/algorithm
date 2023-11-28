T = int(input())

for i in range(T):
    R, P = map(str, input().split())
    R = int(R)
    NP = ""
    for j in range(len(P)):
        NP += P[j] * R
    print(NP)