import math

X_MAX = int(1e12)
ROOT_MAX = int(math.sqrt(X_MAX))


def eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, n + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return sieve


IS_PRIME = eratosthenes(ROOT_MAX)
SET_TPRIME = set()
for i in range(ROOT_MAX + 1):
    if IS_PRIME[i]:
        SET_TPRIME.add(i * i)


def is_TPrime(num: int):
    # A number is T-prime if it has exactly three divisors
    # Which means it is a perfect square and its square root is a prime number
    global SET_TPRIME
    return num in SET_TPRIME


n = int(input())
arr = list(map(int, input().split()))
for a in arr:
    print("YES" if is_TPrime(a) else "NO")
