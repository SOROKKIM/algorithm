dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input()
T = 0

for i in range(len(S)):
    for j in dial:
        if S[i] in j:
            T += dial.index(j)+3
print(T)