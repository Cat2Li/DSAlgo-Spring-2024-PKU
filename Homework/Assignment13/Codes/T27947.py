import heapq


def task():
    arr = list(map(int, input().split()))

    leftheap = []
    mid = arr[0]
    rightheap = []

    mids = [mid]
    for i in range(1, len(arr), 2):
        if (i + 1 == len(arr)):
            break
        x, y = arr[i], arr[i + 1]
        if x > y:
            x, y = y, x
        # x <= y

        if y <= mid:
            heapq.heappush(leftheap, -x)
            heapq.heappush(leftheap, -y)
            heapq.heappush(rightheap, mid)
            mid = -heapq.heappop(leftheap)
        elif x > mid:
            heapq.heappush(leftheap, -mid)
            heapq.heappush(rightheap, x)
            heapq.heappush(rightheap, y)
            mid = heapq.heappop(rightheap)
        else:
            heapq.heappush(leftheap, -x)
            heapq.heappush(rightheap, y)

        mids.append(mid)

    print(len(mids))
    print(" ".join(map(str, mids)))


T = int(input())

for _ in range(T):
    task()
