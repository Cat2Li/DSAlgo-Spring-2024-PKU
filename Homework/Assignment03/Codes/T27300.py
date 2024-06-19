from functools import cmp_to_key

n = int(input())
res = {}


def fmt_value(value):
    if value[-1] == "M":
        return float(value[:-1]) * 1000000
    elif value[-1] == "B":
        return float(value[:-1]) * 1000000000


def cmp_func(value_a, value_b):
    value_a = fmt_value(value_a)
    value_b = fmt_value(value_b)
    if value_a < value_b:
        return -1
    elif value_a > value_b:
        return 1
    else:
        return 0


for i in range(n):
    name, value = input().split("-")
    if name in res:
        res[name].append(value)
    else:
        res[name] = [value]

for key in sorted(res.keys()):
    print(f"{key}: {', '.join(sorted(res[key], key=cmp_to_key(cmp_func)))}")
