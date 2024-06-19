from collections import deque

M, N = map(int, input().split())
arr = map(int, input().split())

word_set = set()
word_queue = deque()

ref_cnt = 0
for word in arr:
    if word not in word_set:
        if len(word_queue) == M:
            word_set.remove(word_queue.popleft())

        word_set.add(word)
        word_queue.append(word)

        ref_cnt += 1

print(ref_cnt)
