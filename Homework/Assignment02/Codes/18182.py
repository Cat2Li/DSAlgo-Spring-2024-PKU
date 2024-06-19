N = int(input())


def solve():
    n, m, b = map(int, input().split())
    skills = [tuple(map(int, input().split())) for _ in range(n)]

    # Timsort is stable
    skills = sorted(skills, key=lambda t: t[1], reverse=True)
    skills = sorted(skills, key=lambda t: t[0])

    cur_t = 0
    cur_t_cnt = 0
    for t, x in skills:
        if cur_t != t:
            cur_t = t
            cur_t_cnt = 0

        if cur_t_cnt == m:
            continue

        assert cur_t_cnt < m
        b -= x
        cur_t_cnt += 1

        if b <= 0:
            print(cur_t)
            return

    print("alive")


for i in range(N):
    solve()
