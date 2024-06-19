L, M = map(int, input().split())
avaliable = [True] * (L + 1)
for _ in range(M):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        avaliable[i] = False
print(avaliable.count(True))
