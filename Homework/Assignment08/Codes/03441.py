from collections import Counter
from itertools import product

N = int(input())

A = []
B = []
C = []
D = []

for i in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab_sum_counter = Counter(map(sum, product(A, B)))
count = 0
for cd_sum in map(sum, product(C, D)):
    count += ab_sum_counter.get(-cd_sum, 0)

print(count)
