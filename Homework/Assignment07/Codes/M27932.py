N, K = map(int, input().split())
arr = sorted(map(int, input().split()))

if K == N:
    print(arr[-1])
elif K == 0:
    if arr[0] == 1:
        print(-1)
    else:
        print(1)
elif (arr[K - 1] < arr[K]):
    print(arr[K - 1])
else:
    print(-1)
