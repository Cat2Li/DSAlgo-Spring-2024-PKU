def solve(n, p, m):
    arr = [i + 1 for i in range(n)]
    res = []
    cur = p - 1
    while len(arr) > 0:
        cur = (cur + m - 1) % len(arr)
        res.append(arr.pop(cur))

    return res


while True:
    n, p, m = map(int, input().split())
    if n == 0 and p == 0 and m == 0:
        break
    result = solve(n, p, m)
    print(",".join(map(str, result)))
