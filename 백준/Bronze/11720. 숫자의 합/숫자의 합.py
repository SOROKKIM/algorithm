N = int(input())
S = list(input())
result = 0

for _ in range(N):
    result += int(S[_])
print(result)