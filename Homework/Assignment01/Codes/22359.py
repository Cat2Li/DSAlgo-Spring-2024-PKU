def ertosthenes(n):
    sieve = [True] * (n + 1)
    
    sieve[0] = False
    sieve[1] = False
    
    for i in range(2, n + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return sieve

N = int(input())
sieve = ertosthenes(N)

for i in range(2, N // 2):
    if sieve[i] and sieve[N - i]:
        print(i, N - i)
        break
else:
    raise ValueError("Goldbach's conjecture is wrong")