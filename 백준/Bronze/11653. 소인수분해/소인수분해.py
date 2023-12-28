def prime_factorization(N):
    i = 2
    factors = []

    while i * i <= N:
        if N % i:
            i += 1
        else:
            N //= i
            factors.append(i)

    if N > 1:
        factors.append(N)

    return factors

N = int(input())
result = prime_factorization(N)
for _ in result:
    print(_)