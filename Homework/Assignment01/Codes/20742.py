def fib(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 1
    assert N > 2
    return fib(N-1) + fib(N-2) + fib(N-3)

N = int(input())
print(fib(N))