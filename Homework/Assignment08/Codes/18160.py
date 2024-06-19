transform = {'W': True, '.': False}


def dfs(x, y):
    global figure, status
    if status[x][y]:
        status[x][y] = False
        l = x - 1
        r = x + 1
        u = y - 1
        d = y + 1
        return 1 + dfs(l, u) + dfs(x, u) + dfs(r, u) + dfs(l, y) + dfs(
            r, y) + dfs(l, d) + dfs(x, d) + dfs(r, d)
    else:
        return 0


T = int(input())
ans = []
for t in range(T):
    n, m = map(int, input().split())
    figure = ['.' * (m + 2)] + ['.{}.'.format(input())
                                for j in range(n)] + ['.' * (m + 2)]
    status = [[transform[figure[i][j]] for j in range(0, m + 2)]
              for i in range(0, n + 2)]
    maxm = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if status[i][j]:
                pre_ans = dfs(i, j)
                if pre_ans > maxm:
                    maxm = pre_ans
    ans.append(maxm)
print('\n'.join(map(str, ans)))
