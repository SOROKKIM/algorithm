import sys

K = int(sys.stdin.readline())
stack = []
sum = 0

for i in range (K):
    N = int(sys.stdin.readline())
    if(N == 0):
        if(stack):
            sum -= stack.pop()
    else :
        stack.append(N)
        sum += N
print(sum)
