n, m = map(int, input().split())
D = [[0] * n for i in range(n)]
A = [[0] * n for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    D[a][a] += 1
    D[b][b] += 1
    A[a][b] = 1
    A[b][a] = 1

L = [[*map(lambda x, y: x - y, D[i], A[i])] for i in range(n)]

print('\n'.join(map(lambda l: ' '.join(map(str, l)), L)))
