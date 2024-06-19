def parse(s: str):
    if s in set("+-*/"):
        return s
    return float(s)


def eval(sgn: str, a: float, b: float):
    if sgn == "+":
        return a + b
    if sgn == "-":
        return a - b
    if sgn == "*":
        return a * b
    if sgn == "/":
        return a / b
    raise ValueError("Invalid operator")


def evalable(sgn, a, b):
    return isinstance(sgn, str) and isinstance(a, float) and isinstance(
        b, float)


args = map(parse, input().split())
stack = []

for arg in args:
    stack.append(arg)

    while len(stack) >= 3:
        sgn = stack[-3]
        a = stack[-2]
        b = stack[-1]
        if evalable(sgn, a, b):
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append(eval(sgn, a, b))
        else:
            break

print("{:.6f}".format(stack[0]))
