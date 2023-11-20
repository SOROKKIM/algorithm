import sys
input = sys.stdin.readline

N = int(input().rstrip())

result = 0

for i in range(N):
    A, B = map(int, input().split())
    result =  A + B
    print(result)