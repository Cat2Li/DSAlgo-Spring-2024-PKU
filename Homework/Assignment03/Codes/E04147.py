def iteration(N, t1, t2, t3):
    if N == 1:
        print(f"{N}:{t1}->{t3}")
    else:
        iteration(N - 1, t1, t3, t2)
        print(f"{N}:{t1}->{t3}")
        iteration(N - 1, t2, t1, t3)


N, t1, t2, t3 = input().split()
N = int(N)
iteration(N, t1, t2, t3)
