version = list(map(int, input().split(".")))

version[-1] += 1  # increment the last number

for i in range(len(version) - 1, 0, -1):
    if version[i] > 9:
        version[i] = 0
        version[i - 1] += 1

print(".".join(map(str, version)))
