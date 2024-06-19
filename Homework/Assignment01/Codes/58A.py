S = list(input())
M = list("hello")

S.reverse()
M.reverse()

while len(M) > 0 and len(S) > 0:
    match = M[-1]
    cur = S.pop()
    
    if cur == match:
        M.pop()

if len(M) == 0:
    print("YES")
else:
    print("NO")