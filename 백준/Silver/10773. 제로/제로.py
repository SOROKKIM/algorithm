K = int(input())
stack = []
sum = 0

for i in range (K):
    N = int(input())
    if(N == 0):
        if(stack):
            sum -= stack.pop()
    else :
        stack.append(N)
        sum += N
print(sum)
