N, M = map(int, input().split())
array = [int(input()) for _ in range(N)]

left, right = 0, 0
for elem in array:
    left = max(left, elem)
    right += elem

while left <= right:
    mid = (left + right) // 2

    count = 1
    sum = 0
    for elem in array:
        if sum + elem > mid:
            count += 1
            sum = elem
        else:
            sum += elem

    if count > M:
        left = mid + 1
    else:
        right = mid - 1

print(left)
