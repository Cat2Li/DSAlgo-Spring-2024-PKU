def parse_expr(s: str):
    expr_list = ["("]
    tmp = ""
    for char in s:
        if char == " ":
            continue
        if char in set("+-*/()"):
            if len(tmp) > 0:
                expr_list.append(tmp)
                tmp = ""
            expr_list.append(char)
        else:
            tmp += char
    if len(tmp) > 0:
        expr_list.append(tmp)
        tmp = ""
    expr_list.append(")")
    return expr_list


def task():
    mid_expr = parse_expr(input())
    sgn_stack = []
    res_stack = []

    for token in mid_expr:
        if token in set("+-"):
            while len(sgn_stack) != 0 and sgn_stack[-1] in set("+-*/"):
                sgn = sgn_stack.pop()
                res_stack.append(sgn)
            sgn_stack.append(token)
        elif token in set("*/"):
            while len(sgn_stack) != 0 and sgn_stack[-1] in set("*/"):
                sgn = sgn_stack.pop()
                res_stack.append(sgn)
            sgn_stack.append(token)
        elif token == "(":
            sgn_stack.append(token)
        elif token == ")":
            while sgn_stack[-1] != "(":
                sgn = sgn_stack.pop()
                res_stack.append(sgn)
            sgn_stack.pop()
        else:
            res_stack.append(token)

    print(" ".join(res_stack))


N = int(input())
for _ in range(N):
    task()
