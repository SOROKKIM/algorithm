A, B = map(str, input().split())
RA = int(A[::-1])
RB = int(B[::-1])

if RA < RB:
    print(RB)
else:
    print(RA)