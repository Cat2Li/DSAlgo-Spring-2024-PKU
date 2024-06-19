import bisect

N = int(input())
arr = [int(input()) for _ in range(N)]
assert len(arr) == N

min_stack = []
max_stack = []
result = 0

for j in range(N):
    while len(min_stack) > 0 and arr[min_stack[-1]] >= arr[j]:
        min_stack.pop()
    while len(max_stack) > 0 and arr[max_stack[-1]] < arr[j]:
        max_stack.pop()
    if len(min_stack) > 0:
        k = bisect.bisect(min_stack,
                          max_stack[-1] if len(max_stack) > 0 else -1)
        if (k != len(min_stack)):
            result = max(result, j - min_stack[k] + 1)

    min_stack.append(j)
    max_stack.append(j)

print(result)
