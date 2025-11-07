text = input()

result = []
strength = 0

for i in range(len(text)):
    if text[i] == '>':
        result.append('>')
        strength += int(text[i + 1])   # explosion strength always exists
    else:
        if strength > 0:
            strength -= 1             # skip (delete) this character
        else:
            result.append(text[i])

print("".join(result))
