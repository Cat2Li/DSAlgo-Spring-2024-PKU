n = int(input())
arr = [*map(int, input().split())]

arr_tuple = [*zip(arr, range(1, n + 1))]
arr_tuple.sort(key=lambda x: x[0])

order = [*zip(*arr_tuple)][1]
avg = 0
for i in range(n):
    avg += arr_tuple[i][0] * (n - i - 1)
avg /= n

print(" ".join(map(str, order)))
print(f"{avg:.2f}")
