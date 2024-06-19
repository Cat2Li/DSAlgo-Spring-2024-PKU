from sys import stdin


def task(ref: str, line: str):
    if len(ref) != len(line):
        print("NO")
        return

    stack = []
    check = 0
    for char in ref:
        stack.append(char)
        while len(stack) != 0 and line[check] == stack[-1]:
            check += 1
            stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")


ref = input()
for line in stdin.readlines():
    line = line.strip()
    task(ref, line)
