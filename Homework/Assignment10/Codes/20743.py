from typing import List

s = input()
stack: List[str] = []
tmp: List[str] = []
for char in s:
    if char == ")":
        while char != "(":
            char = stack.pop()
            tmp.append(char)

        tmp.pop()
        stack.extend(tmp)
        tmp.clear()
        continue
    stack.append(char)

print(''.join(stack))
