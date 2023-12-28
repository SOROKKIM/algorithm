def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [num for num in range(2, limit + 1) if is_prime[num]]


def find_prime_sum_and_min(M, N):
    # M 이상 N 이하의 범위 내에서 소수 찾기
    primes = sieve_of_eratosthenes(N)

    # M 이상 N 이하의 소수들만 남기기
    primes = [prime for prime in primes if prime >= M]

    if not primes:
        return -1, -1  
    prime_sum = sum(primes)
    min_prime = min(primes)

    return prime_sum, min_prime
M = int(input())
N = int(input())
prime_sum, min_prime = find_prime_sum_and_min(M, N)
if prime_sum == -1:
    print(prime_sum)
else:
    print(prime_sum)
    print(min_prime)