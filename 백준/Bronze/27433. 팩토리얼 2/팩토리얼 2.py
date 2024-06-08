import sys

N = int(sys.stdin.readline());

total = 1
for i in range(1, N+1):
    total *= i
print(total)
    