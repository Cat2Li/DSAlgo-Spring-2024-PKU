N, W = map(int, input().split())
L = [tuple(map(int, input().split())) for _ in range(N)]

L.sort(key=lambda t: t[0] / t[1])
res = 0
while L:
    v, w = L.pop()
    if W > w:
        W -= w
        res += v
    else:
        res += v * W / w
        break
print(f"{res:.1f}")
