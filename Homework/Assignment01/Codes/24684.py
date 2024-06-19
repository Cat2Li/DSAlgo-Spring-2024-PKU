Options = [*map(int, input().split())]

record = {}
for option in Options:
    record[option] = record.get(option, 0) + 1
    
record = sorted(record.items(), key=lambda x: x[1])

res = []
max_count = record[-1][1]
while len(record) > 0 and record[-1][1] == max_count:
    option, count = record.pop()
    res.append(option)
res = sorted(res)

res = [str(option) for option in res]
print(" ".join(res))