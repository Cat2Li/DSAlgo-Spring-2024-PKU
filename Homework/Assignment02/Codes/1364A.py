T = int(input())


def solve():
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_arr = sum(arr)

    if sum_arr % X != 0:
        print(N)
        return

    for i in range(len(arr)):
        if arr[i] % X != 0 or (arr[N - 1 - i]) % X != 0:
            print(N - i - 1)
            return

    print(-1)
    return


for _ in range(T):
    solve()
