s = input()

mod = 0
result = []
for i in range(len(s)):
    mod = (mod * 2 + int(s[i])) % 5
    if mod == 0:
        result.append("1")
    else:
        result.append("0")

print("".join(result))
