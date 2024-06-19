def merge(arr, aux, lo, mid, hi):
    for k in range(lo, hi + 1):
        aux[k] = arr[k]

    i = lo
    j = mid + 1
    res = 0
    for k in range(lo, hi + 1):
        if (i > mid):
            arr[k] = aux[j]
            j += 1
        elif (j > hi):
            arr[k] = aux[i]
            i += 1
        elif (aux[j] < aux[i]):
            arr[k] = aux[j]
            j += 1
            res += mid - i + 1
        else:
            arr[k] = aux[i]
            i += 1
    return res


def merge_sort(arr, aux, lo, hi):
    if lo >= hi:
        return 0

    left_rcnt = merge_sort(arr, aux, lo, (lo + hi) // 2)
    right_rcnt = merge_sort(arr, aux, (lo + hi) // 2 + 1, hi)
    merge_rcnt = merge(arr, aux, lo, (lo + hi) // 2, hi)

    return left_rcnt + right_rcnt + merge_rcnt


while True:
    N = int(input())
    if N == 0:
        break

    arr = [int(input()) for _ in range(N)]
    aux = [0 for _ in range(N)]

    res = merge_sort(arr, aux, 0, N - 1)
    print(res)
