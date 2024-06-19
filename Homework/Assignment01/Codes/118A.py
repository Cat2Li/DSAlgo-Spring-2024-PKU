s = input()
vowels = set("aeiouy")

s = s.lower()
result = []
for letter in s:
    if letter in vowels:
        continue
    result.append(".")
    result.append(letter)

print("".join(result))