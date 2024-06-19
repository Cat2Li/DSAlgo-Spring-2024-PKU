from collections import deque


def test():
    N = int(input())
    arr = deque()
    for _ in range(N):
        type, arg = map(int, input().split())
        if type == 1:
            arr.append(arg)
        else:
            # type == 2
            if arg == 1:
                arr.pop()
            else:
                # arg == 0
                arr.popleft()

    if len(arr) == 0:
        print('NULL')
    else:
        print(' '.join(map(str, arr)))


T = int(input())
for _ in range(T):
    test()
