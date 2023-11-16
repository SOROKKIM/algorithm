A = list(map(int, input().split()))
A.sort(reverse=True)

if A[0]==A[1]==A[2]:
    reward = 10000+(A[0]*1000)
elif A[0] == A[1] or A[1] == A[2] or A[0] == A[2]:
    reward = 1000+(A[1]*100)
else:
    reward = A[0]*100
    
print(reward)