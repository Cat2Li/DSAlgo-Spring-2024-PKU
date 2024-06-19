complexities = input().split("+")

def parse(complexity):
    prefix, power = complexity.split("^")
    if prefix[0] == "n":
        number = 1
    else:
        number = int(prefix[:-1])
    return number, int(power)

complexities = [parse(complexity) for complexity in complexities]
complexities.sort(key=lambda x: x[1])

while len(complexities) > 1:
    number, power = complexities.pop()
    if number == 0:
        continue
    else:
        print(f"n^{power}")
        break
else:
    print("n^0")